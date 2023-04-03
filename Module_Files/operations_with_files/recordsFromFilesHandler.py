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

from operations_with_files.fileOperations import FileOperations
from config import separator, default_file_to_read_news


class RecordsFromFilesHandler:      # Class to handle reading records from the files

    # Constructor of the RecordsFromFilesHandler object, have default parameter input_file_path
    def __init__(self, input_file_path=default_file_to_read_news):
        self.input_file_path = input_file_path      # initialization of the self.input_file_path variable
        self.available_amount_of_records = len(self.get_records_without_duplicates())  # initialization of the
        # available_amount_of_records variable by geting amount of records without duplicates

    # function to get amount of records to write to file from the console
    def get_amount_of_records_to_write(self) -> int:
        while True:     # infinite loop untill correct amount entered
            try:        # error handler
                # get value from the console with providing max amount of records to write
                amount_of_records = input("Please define amount of records to write, available amount is " +
                                          str(self.available_amount_of_records) + " (press Enter for default value): ")
                if len(amount_of_records) == 0:             # if nothign was entered
                    amount_of_records = self.available_amount_of_records    # put max value of records to variable
                if int(amount_of_records) > self.available_amount_of_records:   # if entered amount is bigger than available
                    print("Entered amount is bigger than available, please try again: ")
                else:                                       # else - successfull entered amount - break the loop
                    break
            except ValueError:                              # except handler
                print('Entered amount of records is not correct, please try again')
        return int(amount_of_records)                       # return entered amount as int value

    # function to get file path from the console
    @staticmethod
    def get_file_path() -> str:
        while True:     # infinite loop until correct path entered
            try:        # error handler
                # get file path from the console
                file_path = input("Please define path to the file (press Enter for default value): ")
                if len(file_path) == 0:         # if nothing was entered
                    file_path = default_file_to_read_news   # put default value to the variable
                    break   # break the loop
                if not file_path.endswith('.txt') or len(file_path) < 5:    # validation of value entered
                    print('File should have file name and \'.txt\' extension, please try again')
                else:
                    break               # break the loop
            except ValueError:          # exception handler
                print('Entered file path is not correct, please try again')
        return file_path                # return file path as string value

    # function to get unique recordings list without duplicates between general file and observed one
    def get_records_without_duplicates(self) -> list:
        list_of_existed_records = FileOperations.read_from_file()       # get list of records exist in general file
        list_of_new_records = FileOperations.read_from_file(self.input_file_path)   # get list of recordings exist in provided file
        list_of_new_records_without_duplicates = []     # initialization of the empty list to keep unique records
        for record in list_of_new_records:      # go threw all records in provided file
            # check if record contains key-words and not present in existed records list
            if ('News' in record or 'Private ad' in record or 'Weather forecast' in record) and record not in list_of_existed_records:
                list_of_new_records_without_duplicates.append(record)   # append record to list of unique records
        return list_of_new_records_without_duplicates   # return created list of unique recordings

    # function to write records to the file
    def write_new_records_to_the_file(self):
        unique_records = self.get_records_without_duplicates()  # get list of unique records
        amount_of_records_to_write = self.get_amount_of_records_to_write()  # get amount of records to write from console
        if len(unique_records) != 0 and amount_of_records_to_write != 0:    # if list of unique records is not empty
            string_to_write = ''        # initialization of the empty string to hold string to write to file
            for x in range(amount_of_records_to_write):     # go threw all records to write
                string_to_write += unique_records[0] + separator + '\n'   # add record to string + separator
                unique_records.remove(unique_records[0])        # removing added element to add the top element every time
            string_to_write = string_to_write[:len(string_to_write) - 1]
            FileOperations.write_to_file(string_to_write)       # write to file created string
            if amount_of_records_to_write == self.available_amount_of_records:   # if all records was written to the file
                self.removing_processed_file()      # remove file without unique records
        else:
            print('No any unique recording available')

    # function to remove the file
    def removing_processed_file(self):
        try:        # exception handler
            FileOperations.delete_file(self.input_file_path)    # delete file by provided path
            print('File removed successfully due to no unique records available')
        except FileExistsError:         # if not successfully - print exception
            print('Error occurs during file removing')
