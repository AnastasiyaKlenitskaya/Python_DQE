import os.path

from CSV_parsing.config import  all_news_file_path, separator, default_file_to_read_news, pattern_text, pattern_city_timestamp, pattern_ad_exp_date
import re
from CSV_parsing.CSV_files.СSVOperations import CSVOperations
from CSV_parsing.data_models.news import News
from CSV_parsing.data_models.private_ad import PrivateAd
from CSV_parsing.data_models.weather_forecast import WeatherForecast
from datetime import datetime


class FileOperations:
    # function to write provided string to file with path (default or provided)
    @staticmethod
    def write_to_file(string_to_write_to_file: str, file_path=all_news_file_path):
        # normalized_string_to_write = string_to_write_to_file
        normalized_string_to_write = FileOperations.text_normalizing(string_to_write_to_file)
        try:        # exception handler
            if os.path.isfile(file_path):  # If file exists
                # write normalized string to file with provided path and 'a' parameter
                FileOperations.write_to_new_or_existed_file(file_path, 'a', normalized_string_to_write)
            else:
                # write normalized string to file with provided path and 'w' parameter
                FileOperations.write_to_new_or_existed_file(file_path, 'w', normalized_string_to_write)

            csv_writer = CSVOperations()    # initialize CSVOperations object
            # create a csv file with words
            csv_writer.create_csv_with_words(FileOperations.get_dict_of_all_words_with_count_from_file())
            # create a csv file with letters
            csv_writer.create_csv_with_letters(FileOperations.get_dict_of_all_letters_with_count_from_file())

        except BaseException as exception:  # exception handler
            print("Exception occurs during writing file (FileOperations.write_to_file method)", exception)

    # function to write string to file based on provided method
    @staticmethod
    def write_to_new_or_existed_file(file_path: str, method: str, string_to_write_to_file: str):
        with open(file_path, method, encoding="utf-8") as file_to_write:    # open file with path and method
            print(string_to_write_to_file, file=file_to_write)              # print to file provided string

    # function to read records from file
    @staticmethod
    def read_from_file(file_path=all_news_file_path) -> list:
        filtered_records_list = []      # initialization of the empty list to hold records
        if os.path.exists(file_path):   # if file exists
            with open(file_path, 'r', encoding='utf-8') as file_to_read:  # open file to read       # fix = add encoding
                text = file_to_read.read()              # read all the file
            records_list = text.split(separator)        # split the string by separator
            for record in records_list:                 # loop threw all records
                if record != '' and record != '\n':                        # if record is not empty
                    record = FileOperations.text_normalizing(record)    # normalize the string
                    filtered_records_list.append(record.lstrip('\n'))   # append record to the list with removing
                    # '\n' from the left side
        return filtered_records_list                    # return created list with records from file

    # function to parse text to object in accordance with data types
    @staticmethod
    def parse_list_of_records_to_objects(list_of_records):
        # list_of_records = FileOperations.read_from_file()   # getting list of record in file
        list_of_object_records = []     # initialization of the empty list of objects
        for record in list_of_records:      # loop threw all records
            lines = record.split('\n')      # split record by lines
            if not len(lines) <= 2:
                if str(lines[0]).find('News') != -1:    # if record is about news
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, lines[1]) and re.match(pattern_city_timestamp, lines[2]):
                        # initialize a news object and append to list
                        list_of_object_records.append(News(lines[1], lines[2]))
                elif str(lines[0]).find('Private ad') != -1:   # if record is about private ad
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, lines[1]) and re.match(pattern_ad_exp_date, lines[2]):
                        # get data in provided format
                        expiration_date = datetime.strptime(lines[2][14:24], '%Y-%m-%d').date()
                        # initialize an ad object and append to list as a string
                        list_of_object_records.append(PrivateAd(lines[1], expiration_date))
                elif str(lines[0]).find('Weather forecast') != -1:   # if record is about weather forecast
                    if re.match(pattern_text, lines[1]) and re.match(pattern_text, lines[2]):
                        # initialize weather forecast object with temp location
                        forecast = WeatherForecast(lines[1], 'temp')
                        forecast.location = lines[2]        # correct forecast to existed in file text
                        # (it's necessary in accordance with weather forecast class constructor)
                        list_of_object_records.append(forecast)     # append created object as string to list
        return list_of_object_records       # return list of objects

    # function to remove the file
    @staticmethod
    def delete_file(file_path: str):
        try:
            if os.path.isfile(file_path):       # if file by path exists
                os.remove(file_path)            # remove file
                print('File removed successfully due to no unique records available')
            else:
                print('File was not removed, incorrect file path')
        except FileExistsError:         # if not successfully - print exception
            print('Error occurs during file removing')

    # function to normalize string from previous home task
    @staticmethod
    def text_normalizing(string_to_normalize: str) -> str:
        string_to_normalize = string_to_normalize.lower().capitalize()  # get string, normalize and capitalize it
        flag_to_change_case = False                                     # initialize flag with false as default
        for x in range(len(string_to_normalize) - 2):                   # loop threw the string
            if flag_to_change_case and string_to_normalize[x].isalpha():  # check flag and current element is a char
                # changing case of found char
                string_to_normalize = string_to_normalize[0:x] + string_to_normalize[
                    x].swapcase() + string_to_normalize[
                                    x + 1: len(
                                        string_to_normalize)]
                flag_to_change_case = False  # changing back flag value
            # check to detect end of sentence (except file extension) to change flag value
            if string_to_normalize[x] in ['\n', '\t', '!', '?'] or \
                    (string_to_normalize[x] == '.' and not string_to_normalize[x + 1].isalpha()):
                flag_to_change_case = True  # changing flag value
        return string_to_normalize      # return normalized string

    # Function to get dict with all words and amount of its appearance in provided file
    @staticmethod
    def get_dict_of_all_words_with_count_from_file(file_path=all_news_file_path) -> dict:
        filtered_records_list = FileOperations.read_from_file(file_path)      # get list of records
        dict_of_words = {}       # initialization of empty dict to hold words, and it's count of appearance
        separated_list_of_words = []     # initialization of empty list to hold words
        for record in filtered_records_list:       # loop threw list of records
            separated_list_of_words.append(re.findall(r"[\w'-]+", record.lower()))     # separating record by words
        for list_of_words in separated_list_of_words:   # loop threw list of words
            for word in list_of_words:      # loop threw list of the words
                # word = word.lower()      # converting to lowercase current word
                if word.isalpha() or word.find('\'') != -1:          # if current item is a word
                    if word in dict_of_words:   # if word already present in the dict
                        dict_of_words[word] += 1    # increase counter
                    else:                   # if not present
                        dict_of_words[word] = 1     # append with counter = 1
        return dict_of_words                # return dict with words and count of appearance

    # Function to get dict with all letters, and it's count from provided file
    @staticmethod
    def get_dict_of_all_letters_with_count_from_file(file_path=all_news_file_path) -> list:
        filtered_records_list = FileOperations.read_from_file(file_path)    # get list of records
        dict_of_letters = {}                                            # initialization of empty dict to hold letters
        dict_of_capital_letters = {}                             # initialization of empty dict to hold capital letters
        separated_list_of_words = []                            # initialization of empty list to hold words
        for record in filtered_records_list:                    # loop threw all the records
            separated_list_of_words.append(re.split(r'\W+', record))   # separating records to the words
        for list_of_words in separated_list_of_words:           # loop threw separated list of words
            for word in list_of_words:                          # loop threw all words in the list of words
                if word.isalpha():                              # if item is a word
                    for char in word:                           # loop threw every char in the word
                        if char.isupper():                      # if char is in capital case
                            if char in dict_of_capital_letters:     # if char already in dict
                                dict_of_capital_letters[char] += 1  # increase count of appearance
                            else:                               # else
                                dict_of_capital_letters[char] = 1   # append char with count = 1
                        elif char in dict_of_letters:           # else if non-capital and already in dict
                            dict_of_letters[char] += 1          # increase counter
                        else:                                   # else
                            dict_of_letters[char] = 1           # append with counter = 1
        list_with_lists_of_records = []                         # initialization of the list to hold lists with words
        lowercased_dict_of_capital_letters = {}                 # initialization dict with lowercased capital letters
        counter_of_all_letters = 0                              # initialization of the counter

        for key in dict_of_capital_letters:                     # loop threw dict of the capital letters
            lowercased_dict_of_capital_letters[key.lower()] = dict_of_capital_letters[key]  # append lowercased key
            # and count to the dict
            if key.lower() in dict_of_letters:      # if observed letter already present in list of letters
                dict_of_letters[key.lower()] += 1   # increase its counter
            else:                                   # else
                dict_of_letters[key.lower()] = 1    # append and set counter = 1

        for key in dict_of_letters:                             # loop threw dict of the all letters
            counter_of_all_letters += dict_of_letters[key]  # increase counter of all letters by count of current letter
        for key in dict_of_capital_letters:                     # loop threw dict of the capital letters
            counter_of_all_letters += dict_of_capital_letters[key]  # increase counter of all letters by count of
            # current letter

        for key in dict_of_letters:                     # loop threw dict of letters
            sub_list = [key]                            # initialization of the sub-list with all data for each letter
            if key in lowercased_dict_of_capital_letters:   # if key is present in dict with lowercased capital letters
                sub_list.append(dict_of_letters[key] + lowercased_dict_of_capital_letters[key])  # append to the list
                # count of letter appearance
                sub_list.append(lowercased_dict_of_capital_letters[key])    # append to the list amount of uppercase
                # appearance
            else:                                       # if key was not in the uppercase dict
                sub_list.append(dict_of_letters[key])   # append amount of appearance
                sub_list.append(0)                      # append 0 - appearance of uppercase letters
            sub_list.append(sub_list[1] * 100 / counter_of_all_letters)  # append percentage of uppercase letters
            list_with_lists_of_records.append(sub_list)     # append sub list to the general list

        return list_with_lists_of_records           # return list with lists for every letter

    # function to get file path from the console
    @staticmethod
    def get_file_path(extension: str):
        while True:     # infinite loop until correct path entered
            try:        # error handler
                # get file path from the console
                file_path = input("Please define path to the file (press Enter for default value): ")
                if len(file_path) == 0:         # if nothing was entered
                    file_path = default_file_to_read_news   # put default value to the variable
                if not file_path.endswith(extension) or len(file_path) < (len(extension) + 1):  # validation of value entered
                    print('File should have file name and \'.txt\' extension, please try again')
                else:
                    break               # break the loop
            except ValueError:          # exception handler
                print('Entered file path is not correct, please try again')
        return file_path                # return file path as string value

# function to get amount of records to write to file from the console
    @staticmethod
    def get_amount_of_records_to_write(available_amount_of_records) -> int:
        while True:     # infinite loop until correct amount entered
            try:        # error handler
                # get value from the console with providing max amount of records to write
                amount_of_records = input("Please define amount of records to write, available amount is " +
                                          str(available_amount_of_records) + " (press Enter for default value): ")
                if len(amount_of_records) == 0:             # if nothing was entered
                    amount_of_records = available_amount_of_records    # put max value of records to variable
                if int(amount_of_records) > available_amount_of_records:   # if entered amount is bigger than available
                    print("Entered amount is bigger than available, please try again: ")
                else:                                       # else - successful entered amount - break the loop
                    break
            except ValueError:                              # except handler
                print('Entered amount of records is not correct, please try again')
        return int(amount_of_records)                       # return entered amount as int value

    @staticmethod
    def is_file_exist(file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False
