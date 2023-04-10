# Homework 6
#
# expand previous Homework 5 with additional class, which allows to provide records by text file: - done, checked
#
# + 1. Define your input format (one or many records) - done, checked
#
# 2. Default folder or user provided file path -done, checked
#
# 3. Remove file if it was successfully processed - done, checked
#
# 4. Apply case normalization functionality from Homework 3/4 - done, checked

from CSV_parsing.operations_with_files.file_operations import FileOperations
from CSV_parsing.config import separator, default_file_to_read_news
from CSV_parsing.sql import SQLManager


class RecordsFromFilesHandler:      # Class to handle reading records from the files

    # Constructor of the RecordsFromFilesHandler object, have default parameter input_file_path
    def __init__(self, input_file_path=default_file_to_read_news):
        self.input_file_path = input_file_path      # initialization of the self.input_file_path variable
        self.available_amount_of_records = len(self.get_records_without_duplicates())  # initialization of the
        # available_amount_of_records variable by getting amount of records without duplicates

    # function to get unique recordings list without duplicates between general file and observed one
    def get_records_without_duplicates(self) -> list:
        list_of_existed_records = FileOperations.read_from_file()       # get list of records exist in general file
        list_of_new_records = FileOperations.read_from_file(self.input_file_path)   # get list of recordings exist
        list_of_new_records_without_duplicates = []     # initialization of the empty list to keep unique records
        for record in list_of_new_records:      # go threw all records in provided file
            # check if record contains key-words and not present in existed records list
            if ('News' in record or 'Private ad' in record or 'Weather forecast' in record) and record not in list_of_existed_records:
                list_of_new_records_without_duplicates.append(record)   # append record to list of unique records
        return list_of_new_records_without_duplicates   # return created list of unique recordings

    # function to write records to the file
    def write_new_records_to_the_file(self):
        db = SQLManager()   # initialize db object
        unique_records = self.get_records_without_duplicates()  # get list of unique records
        # list_of_objects = []
        # get amount of records to write from console
        amount_of_records_to_write = FileOperations.get_amount_of_records_to_write(self.available_amount_of_records)
        if len(unique_records) != 0 and amount_of_records_to_write != 0:    # if list of unique records is not empty
            string_to_write = ''        # initialization of the empty string to hold string to write to file
            for x in range(amount_of_records_to_write):     # go threw all records to write
                # write object to db
                obj_to_write = FileOperations.parse_list_of_records_to_objects([unique_records[0]])
                if len(obj_to_write) != 0:
                    db.write_obj_to_db(obj_to_write[0])
                # list_of_objects.append(FileOperations.parse_list_of_records_to_objects([unique_records[0]]))
                string_to_write += unique_records[0] + separator + '\n'   # add record to string + separator
                unique_records.remove(unique_records[0])   # removing added element to add the top element every time
            string_to_write = string_to_write[:len(string_to_write) - 1]    # remove last \n element
            FileOperations.write_to_file(string_to_write)       # write to file created string
            if amount_of_records_to_write == self.available_amount_of_records:  # if all records was written to the file
                FileOperations.delete_file(self.input_file_path)      # remove file without unique records
        else:
            print('No any unique recording available')
        db.cursor.close()       # close db cursor
        db.connection.close()   # close db connection
