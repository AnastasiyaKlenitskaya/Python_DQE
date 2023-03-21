import os.path


class FileOperations:
    @staticmethod
    def write_to_file(string_to_write_to_file: str):
        if os.path.isfile('news_feed.txt'):  # If file exists
            with open('news_feed.txt', 'a') as file_to_write:   # Open file in mode to add new text
                print(string_to_write_to_file, file=file_to_write)  # print to file given argument
        else:                                                   # If file is not exist
            with open('news_feed.txt', 'w') as file_to_write:       # Create and open file
                print(string_to_write_to_file, file=file_to_write)  # print to file given argument
