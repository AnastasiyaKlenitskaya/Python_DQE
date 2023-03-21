import os.path
from config import all_news_file_path, default_file_to_read_news, separator


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
                    filtered_records_list.append(record.lstrip('\n'))   # append record to the list with removing '\n' from the left side
        return filtered_records_list                    # return created list

    # function to remove the file
    @staticmethod
    def delete_file(file_path) -> bool:
        if os.path.isfile(file_path):       # if file by path exists
            os.remove(file_path)            # remove file
            return True
        else:
            return False

    # function to normalize string from previous hometask
    @staticmethod
    def text_normalizing(string_to_normalize: str) -> str:
        string_to_normalize = string_to_normalize.lower().capitalize()  # get string, normalize and capitalize it
        flag_to_change_case = False                                     # initialize flag with false as default
        for x in range(len(string_to_normalize) - 2):                   # loop threw the string
            if flag_to_change_case and string_to_normalize[x].isalpha(): # check flag and that current element is a char
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
