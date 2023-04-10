from CSV_parsing.operations_with_files.file_operations import FileOperations
from CSV_parsing.config import default_file_path_to_json_file, pattern_text, pattern_city_timestamp, default_file_path_to_xml_file
import xml.etree.ElementTree as ET
from CSV_parsing.data_models.record import Record
from CSV_parsing.data_models.news import News
from CSV_parsing.data_models.private_ad import PrivateAd
from CSV_parsing.data_models.weather_forecast import WeatherForecast
from datetime import datetime
import re
from CSV_parsing.sql import SQLManager


"""Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:

1.Define your input format (one or many records)

2.Default folder or user provided file path

3.Remove file if it was successfully processed"""


class XMLManager:
    # class constructor with file_path as argument with default value defined
    def __init__(self, file_path=default_file_path_to_xml_file):
        self.file_path = file_path  # default file path
        # initialization of a self variable to hold list of objects from xml file
        self.list_of_object_records = self.get_objs_list_from_xml_file()
        # initialization of a self variable to hold list of unique records from json file
        self.unique_objects = self.get_list_of_unique_object_from_xml()
        # initialization of a self variable to hold amount of unique records
        self.available_amount_of_record_to_write = len(self.unique_objects)

    # function to get objects from xml file data
    def get_objs_list_from_xml_file(self):
        list_of_object_records = []     # initialization of empty list to hold parsed objects
        try:        # exception handler
            xml_file = ET.parse(self.file_path)     # parsing xml file
            root = xml_file.getroot()               # getting root element of the xml file
            for element in root.findall('Record'):   # loop threw all 'Record' elements in file
                main_text = element.find('main_text').text.strip()   # parsing text from 'main_text' element
                second_text = element.find('secondary_text').text.strip()  # parsing text from 'secondary_text' element
                if element.attrib['type'] == 'News':        # for elements with attribute type = 'News'
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, main_text) and re.match(pattern_city_timestamp, second_text):
                        # initialize News object with parsed and normalized data
                        news_object = News(FileOperations.text_normalizing(main_text),
                                           FileOperations.text_normalizing(second_text))
                        list_of_object_records.append(news_object)      # append initialized object to the list
                elif element.attrib['type'] == 'Private ad':    # for elements with attribute type = 'Private ad'
                    exp_date = datetime.strptime(second_text, '%Y-%m-%d').date()    # parse date to proper format
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, main_text):
                        # initialize Private ad object with parsed and normalized data
                        private_ad_obj = PrivateAd(FileOperations.text_normalizing(main_text), exp_date)
                        list_of_object_records.append(private_ad_obj)   # append initialized object to the list
                # for elements with attribute type = 'Weather forecast'
                elif element.attrib['type'] == 'Weather forecast':
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, main_text) and re.match(pattern_text, second_text):
                        # initialize Weather forecast object with parsed and normalized text and temp value
                        forecast_obj = WeatherForecast(FileOperations.text_normalizing(main_text), 'temp')
                        # applying correct data from file to object field
                        forecast_obj.location = FileOperations.text_normalizing(second_text)
                        list_of_object_records.append(forecast_obj)  # append initialized object to the list
        except FileNotFoundError as error:      # error handler
            print("Error occurs during open file: ", error)
        return list_of_object_records

    # function to get list of unique objects by comparing existed and objects from file data
    def get_list_of_unique_object_from_xml(self):
        list_of_unique_objects = []  # initialize list to hold unique objects
        list_of_existed_objects = FileOperations.parse_list_of_records_to_objects(FileOperations.read_from_file())  # get list of existed objects
        for new_object in self.list_of_object_records:  # loop threw list of object from file
            flag = False        # initialization of the flag
            for existed_object in list_of_existed_objects:  # loop threw list of existed objects
                if Record.is_equal(new_object, existed_object):  # call the function to compare 2 objs
                    flag = True     # if equal set flag to True - record already exist
            if not flag:        # if flag was not set to True
                list_of_unique_objects.append(new_object)   # append found unique obj to the list
        return list_of_unique_objects   # return defined list with unique objects

    # function to write unique objects to the file
    def write_unique_records_to_file(self):
        db = SQLManager()       # initialize db object
        # get amount of records to write
        amount_objs_to_write = FileOperations.get_amount_of_records_to_write(self.available_amount_of_record_to_write)
        string_to_write = ''  # initialization of an empty string
        # if available amount to write != 0 and selected amount to write != 0
        if self.available_amount_of_record_to_write != 0 and amount_objs_to_write != 0:
            for iteration in range(amount_objs_to_write):  # loop to fill in string by objects
                db.write_obj_to_db(self.unique_objects[0])   # write object to db
                string_to_write += self.unique_objects[0].convert_to_string() + '\n'  # fill in string variable
                self.unique_objects.remove(self.unique_objects[0])  # remove obj from list to avoid duplicated
            # write created string to file
            FileOperations.write_to_file(string_to_write[:len(string_to_write) - 1])
            if amount_objs_to_write == self.available_amount_of_record_to_write:  # if we wrote max amount of objects
                FileOperations.delete_file(self.file_path)  # remove file
        elif self.available_amount_of_record_to_write == 0:  # if no available object to write
            FileOperations.delete_file(self.file_path)  # remove file
        else:  # else
            print('No any unique recording available')  # print that no unique objects available
        db.cursor.close()               # close db cursor
        db.connection.close()           # close  db connection
