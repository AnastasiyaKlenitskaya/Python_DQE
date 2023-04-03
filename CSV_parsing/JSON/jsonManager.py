"""Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:

1.Define your input format (one or many records) - done, checked

2.Default folder or user provided file path - done, checked

3.Remove file if it was successfully processed - done, checked"""

from operations_with_files.fileOperations import FileOperations
from config import default_file_path_to_json_file, pattern_text, pattern_city_timestamp
import json
import re
from data_models.news import News
from data_models.privateAd import PrivateAd
from data_models.weatherForecast import WeatherForecast
from datetime import datetime


class JsonManager:
    def __init__(self):  # class constructor
        self.file_path = default_file_path_to_json_file  # default file path
        # initialization of a self variable to hold list of records from json file
        self.list_of_records = self.parse_json_file_data_to_objs_list(self.get_json_file_data())
        # initialization of a self variable to hold list of unique records from json file
        self.unique_objects = self.get_list_of_unique_objects()
        # initialization of a self variable to hold amount of unique records
        self.available_amount_of_record_to_write = len(self.unique_objects)

    # function to get data from json file
    def get_json_file_data(self) -> dict:
        try:
            with open(self.file_path, "r", encoding="utf-8") as read_file:  # open json file
                data = json.load(read_file)  # get data from json to variable as a dict
            return data  # return dict with data from json file
        except FileNotFoundError as error:
            print("Error occurs during open file: ", error)

    # function to parce data from dict to list of objects
    @staticmethod
    def parse_json_file_data_to_objs_list(data: dict) -> list:
        list_of_objects = []  # initialization of the empty list to hold list of objects
        for news_record in data['News']:  # loop threw news items in dict
            # if text in record are validated by regular expressions
            if re.match(pattern_text, news_record['newsText']) and re.match(pattern_city_timestamp,
                                                                            news_record['cityTimestamp']):
                # initialization of the news object
                news_object = News(FileOperations.text_normalizing(news_record['newsText']),
                                   FileOperations.text_normalizing(news_record['cityTimestamp']))
                list_of_objects.append(news_object)  # append initialized object to the list
        for ad_record in data['Private ad']:  # loop threw private ad items in dict
            try:
                exp_date = datetime.strptime(ad_record['timestamp'], '%Y-%m-%d').date()
                ad_text = FileOperations.text_normalizing(ad_record['advertisementText'])
                # if text in record are validated by regular expressions
                if re.match(pattern_text, ad_text):  # getting data in proper format
                    # initialization of the private ad object
                    private_ad_object = PrivateAd(ad_text, exp_date)
                    list_of_objects.append(private_ad_object)  # append initialized object to the list
            except ValueError as error:
                print('Wrong data format in provided record during parsing', ad_record, "error: ", error)
        for forecast_record in data['Weather forecast']:  # loop threw weather forecast items in dict
            forecast_text = FileOperations.text_normalizing(forecast_record['forecastText'])
            forecast_location = FileOperations.text_normalizing(forecast_record['location'])
            if re.match(pattern_text, forecast_text) and re.match(pattern_text, forecast_location):
                forecast = WeatherForecast(forecast_text, 'temp')  # initialization of forecast object
                forecast.location = forecast_location   # correct forecast location text to existed in file text
                list_of_objects.append(forecast)  # append initialized object to the list
        return list_of_objects  # return list of objects

    # function to get list of unique object by comparative existed objects and new once
    def get_list_of_unique_objects(self):
        list_of_existed_objects = FileOperations.parse_list_of_records_to_objects()  # get list of existed objects
        list_of_unique_objects = []  # initialize list to hold unique objects
        for new_object in self.list_of_records:  # loop threw new list of records (objects)
            flag = False  # flat to find unique objects
            for existed_object in list_of_existed_objects:  # loop threw existed objects
                # if string values of these objects are equal
                if new_object.convert_to_string() == existed_object.convert_to_string():
                    flag = True  # set the flag
            if not flag:  # if flag was not set
                list_of_unique_objects.append(new_object)  # append unique object
        return list_of_unique_objects  # return list of the unique objects

    # function to write unique records to the file
    def write_unique_records_to_file(self):
        # get amount of objects to write to file
        # self.unique_objects = self.get_list_of_unique_objects()
        amount_objs_to_write = FileOperations.get_amount_of_records_to_write(self.available_amount_of_record_to_write)
        string_to_write = ''  # initialization of an empty string
        # if records to write are available and amount of objects to write by user is not = 0
        if self.available_amount_of_record_to_write != 0 and amount_objs_to_write != 0:
            for iteration in range(amount_objs_to_write):  # loop to fill in string by objects
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
