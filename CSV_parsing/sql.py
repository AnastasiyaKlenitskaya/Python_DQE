import sqlite3
from CSV_parsing.config import default_file_path_to_db
from CSV_parsing.data_models.news import News
from datetime import datetime
from CSV_parsing.data_models.private_ad import PrivateAd
from CSV_parsing.data_models.weather_forecast import WeatherForecast
from CSV_parsing.data_models.record import Record
import re

"""
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:

1.Different types of records require different data tables

2.New record creates new row in data table

3.Implement “no duplicate” check."""


class SQLManager:
    def __init__(self):
        self.connection = sqlite3.connect(default_file_path_to_db)      # connection with sqlite initialization
        self.cursor = self.connection.cursor()      # cursor initialization
        # list of params to news table
        self.params_list_news = ['news_text TEXT', 'news_city TEXT', 'news_timestamp TEXT']
        # list of params to private ad table
        self.params_list_ad = ['ad_text TEXT', 'actual_until TEXT', 'days_left TEXT']
        # list of params to weather forecast table
        self.params_list_forecast = ['forecast_text TEXT', 'forecast_city TEXT', 'weather TEXT']
        self.params_list = []   # list to hold params of current table

    # function to check if table exist and create it if not, got table name and list of params as arguments
    def create_table_if_not_exist(self, table_name: str, params_list: list):
        # initialization of params string varaiable to hold all params
        params = '(id integer not null primary key autoincrement, ' + ', '.join(params_list) + ')'
        # initialization of variable with whole text to 'create table' request
        create_table_text = "create table if not exists " + table_name + params
        self.cursor.execute(create_table_text)  # executing 'create table' command
        self.connection.commit()    # commit command

    # main function to write provided object to db, will call all the checks inside
    def write_obj_to_db(self, record_object):
        dict_of_params = list(record_object.__dict__.items())   # get list of the obj params
        table_name = str(dict_of_params[0][1]).strip('-')   # get table name
        record_text = str(dict_of_params[1][1])         # get main text of the record
        secondary_text = str(dict_of_params[2][1])      # get second line text the will be parsed
        list_of_values = [record_text]              # convert string with main text to list to extend it later by another arguments

        if table_name == 'News ':       # for News table
            # check that table exist
            self.create_table_if_not_exist(table_name, self.params_list_news)
            # extend list of values by parsed second line text
            list_of_values.extend(SQLManager.parse_news_second_text(secondary_text))
            self.params_list = self.params_list_news    # get list of params for news table to avoid check later
        elif table_name == 'Private ad ':    # for Private_ad table
            table_name = 'Private_ad '  # rename table name to proper format
            # check that table exist
            self.create_table_if_not_exist(table_name, self.params_list_ad)
            # extend list of values by parsed second line text
            list_of_values.extend(SQLManager.parse_private_ad_second_text(secondary_text))
            self.params_list = self.params_list_ad      # get list of params for private ad table
        elif table_name == 'Weather Forecast ':  # for Weather_forecast table
            table_name = 'Weather_forecast '    # rename table name to proper format
            # check that table exist
            self.create_table_if_not_exist(table_name, self.params_list_forecast)
            # extend list of values by parsed second line text
            list_of_values.extend(SQLManager.parse_weather_forecast_second_text(secondary_text))
            self.params_list = self.params_list_forecast    # get list of params for weather forecast table

        # check that provided object is not present in db by select all records, parse them to object and compare
        if self.is_record_unique(record_object):
            self.insert_for_table(table_name, self.params_list, list_of_values)     # insert provided obj to db
        else:
            print('Record already exist')

    # function to parse second text of news obj
    @staticmethod
    def parse_news_second_text(record_text: str):
        #  'Krakow, 2023-03-29 19:41'
        try:    # error handler
            timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"    # regular expression to find date
            match = re.search(timestamp_pattern, record_text)       # search of timestamp pattern in provided string
            # params_list = []            # initialize
            if match:           # if match found
                # params_list.append(record_text[:match.start() - 2].strip())
                # params_list.append(match.group(0))
                return [record_text[:match.start() - 2].strip(), match.group(0)]       # return parsed string in list
        except ValueError as error:
            print(error, " occurs during parsing news second text to city and timestamp")

    # function to parse second text of private ad obj
    @staticmethod
    def parse_private_ad_second_text(record_text: str):
        # Actual until: 2023-03-29, 7 days left
        match = re.search(r'\d{4}-\d{2}-\d{2}', record_text)    # search of date pattern in provided string
        return [match.group(0), record_text[match.end() + 2:]]  # return parsed string in list

    # function to parse second text of weather forecast obj
    @staticmethod
    def parse_weather_forecast_second_text(record_text: str):
        # Weather for Krakow: temperature is 27, hail
        city = re.search(r'Weather for (\w+):', record_text)    # search substring by regexp in provided string
        temp_start = record_text.find("temperature is ") + len("temperature is ")   # get location of substring from provided string
        temp = record_text[temp_start:]     # get substring from provided string
        return [city.group(1), temp]    # return parsed string in list

    # function to make insert to db by provided table name, params and values list
    def insert_for_table(self, table_name: str, params_list: list, values_list: list):
        # crop items in params list by param name (without param type) -> create string with params
        params = '(' + ', '.join([item.split(' ')[0] for item in params_list]) + ')'
        values = '(\"' + '\", \"'.join(values_list) + '\")'     # create string with values
        insert_string = "insert into main." + table_name + params + ' values ' + values  # create string with insert text
        # print(insert_string)
        self.cursor.execute(insert_string)  # execute created insert command
        self.connection.commit()        # commit executed insert command

    # function to get all records from db and retun list of object for provided table name
    def select_all_record_from_db(self, table_name) -> list:
        list_of_object_from_db = []     # initialize empty list to hold objs
        self.cursor.execute('select * from main.' + table_name + ';')  # select all records from provided table name
        records = self.cursor.fetchall()        # get results for select
        for record in records:      # loop threw all records from db
            if table_name == 'News ':   # if select was from News table
                # append created News object with selected params to the list
                list_of_object_from_db.append(News(record[1], record[2] + ", " + record[3]))
            elif table_name == 'Private_ad ':     # if select was from Private_ad table
                exp_date = datetime.strptime(str(record[2]), '%Y-%m-%d').date()  # convert string with date to proper format
                # append created Private ad object with selected and parsed params to the list
                list_of_object_from_db.append(PrivateAd(record[1], exp_date))
            elif table_name == 'Weather_forecast ':   # if select was from Weather_forecast table
                forecast_text = 'Weather for ' + record[2] + ': temperature is ' + record[3]    # convert forecast text to proper format string
                forecast_obj = WeatherForecast(record[1], 'temp')   # initialize Weather forecast obj with temp value
                forecast_obj.location = forecast_text   # put correct value for created object
                list_of_object_from_db.append(forecast_obj)  # append created and corrected object to the list
        return list_of_object_from_db       # return list of objects from db

    # function to check that provided object is unique, calls function to get list of all records from proper table inside
    def is_record_unique(self, obj_to_check) -> bool:
        list_of_existed_in_db_objs = []  # initialize empty list of object that will filled in by records from db
        if isinstance(obj_to_check, News):  # if provided object is News class
            list_of_existed_in_db_objs = self.select_all_record_from_db('News ')    # get all records from this table
        elif isinstance(obj_to_check, PrivateAd):   # if provided object is Private ad class
            list_of_existed_in_db_objs = self.select_all_record_from_db('Private_ad ')  # get all records from this table
        elif isinstance(obj_to_check, WeatherForecast):  # if provided object is Weather forecast class
            list_of_existed_in_db_objs = self.select_all_record_from_db('Weather_forecast ')    # get all records from this table

        for item in list_of_existed_in_db_objs:     # loop threw all records from db
            if Record.is_equal(item, obj_to_check):     # if provided object is equal to iterated one
                return False        # return false
        return True     # if equal object was not found - return true -> provided object is unique
