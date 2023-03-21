import csv
from config import default_file_path_to_csv_file

"""Calculate number of words and letters from previous Homeworks 5/6 output test file.

Create two csv:

1.word-count (all words are preprocessed in lowercase)

2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)

CSVs should be recreated each time new record added.

"""


# class to create csv files
class CSVOperations:
    def __init__(self, path=default_file_path_to_csv_file):
        # initialization of the variable holding path to csv file that will be created
        self.file_path = path

    # function to create csv file with words and count of it's appearance
    @staticmethod
    def create_csv_with_words(dict_of_words: dict):
        file_path = default_file_path_to_csv_file + '/words.csv'  # get path to file that will be created
        try:  # error handler
            # open file to write
            with open(file_path, 'w', newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)  # initialization of the file writer
                for key, value in dict_of_words.items():  # loop threw dict with words
                    writer.writerow([key, value])  # write dict item to the file
        except BaseException as exception:  # exception handler
            print(exception)  # print appeared exception

    # function to create csv file with letters
    @staticmethod
    def create_csv_with_letters(list_of_dicts_with_letters: list):
        file_path = default_file_path_to_csv_file + '/letters.csv'  # get path to file that will be created
        fieldnames = ["letter", "count_all", "count_uppercase", "percentage"]  # list of headers
        try:  # error handler
            with open(file_path, 'w', newline="", encoding="utf-8") as csv_file:  # open file to write
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # initialization of the file writer
                writer.writeheader()  # write headers
                for sublist in list_of_dicts_with_letters:  # for each provided list item
                    # write line with provided date
                    writer.writerow({'letter': sublist[0], 'count_all': sublist[1],
                                     'count_uppercase': sublist[2], 'percentage': sublist[3]})
        except BaseException as exception:      # exception handler
            print(exception)        # print found exception
