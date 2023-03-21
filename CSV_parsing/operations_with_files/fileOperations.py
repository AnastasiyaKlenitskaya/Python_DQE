import os.path
from config import all_news_file_path, separator
import re
from CSVFiles.CSVOperations import CSVOperations


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
            csv_writer = CSVOperations()
            csv_writer.create_csv_with_words(FileOperations.get_dict_of_all_words_with_count_from_file())
            csv_writer.create_csv_with_letters(FileOperations.get_dict_of_all_letters_with_count_from_file())
        except BaseException as exception:  # exception handler
            print(exception)    # print exception

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
            with open(file_path, 'r') as file_to_read:  # open file to read
                text = file_to_read.read()              # read all the file
            records_list = text.split(separator)        # split the string by separator
            for record in records_list:                 # loop threw all records
                if record != '':                        # if record is not empty
                    record = FileOperations.text_normalizing(record)    # normalize the string
                    filtered_records_list.append(record.lstrip('\n'))   # append record to the list with removing
                    # '\n' from the left side
        return filtered_records_list                    # return created list

    # function to remove the file
    @staticmethod
    def delete_file(file_path) -> bool:
        if os.path.isfile(file_path):       # if file by path exists
            os.remove(file_path)            # remove file
            return True
        else:
            return False

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
            separated_list_of_words.append(re.split(r"\W+", record))    # separating record by words
        for list_of_words in separated_list_of_words:   # loop threw list of words
            for word in list_of_words:      # loop threw list of the words
                word = word.lower()         # converting to lowercase current word
                if word.isalpha():          # if current item is a word
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
