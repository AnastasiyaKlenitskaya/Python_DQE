from CSV_parsing.config import default_file_path_to_json_file, default_file_path_to_xml_file
from CSV_parsing.operations_with_files.file_operations import FileOperations
from CSV_parsing.operations_with_files.records_from_files_handler import RecordsFromFilesHandler
from CSV_parsing.data_models.news import News
from CSV_parsing.data_models.weather_forecast import WeatherForecast
from CSV_parsing.data_models.private_ad import PrivateAd
from CSV_parsing.JSON.jsonManager import JsonManager
from CSV_parsing.XML.xmlManager import XMLManager
from CSV_parsing.sql import SQLManager
from datetime import datetime
from datetime import timedelta

class NewsGeneratorMenu:

    def __init__(self):
        self.file_to_write = FileOperations()  # initialization of local variable with object of FileOperations class
        self.db = SQLManager()      # initialize db object

    # Function to get info from console input
    @staticmethod
    def get_input_from_console() -> str:
        menu_input = input(">>> ")  # input selected option from the console
        return menu_input.lower()  # return lowercased input text

    # Initial menu where we select to read or to generate the news
    def initial_menu(self):
        while True:     # loop until exit
            print("Hi! I can read news from file or generate new one, what would you prefer ?:\n"
                  "\t1. Generate news menu\n"
                  "\t2. Read records from text file\n"
                  "\t3. Read records from JSON file\n"
                  "\t4. Read records from XML file\n"
                  "\t0. Exit")
            choice = NewsGeneratorMenu.get_input_from_console()     # get input from the console
            if choice.find("generate") != -1 or choice == "1":     # if user select generate
                self.generate_news_menu()                                   # open menu for generating news
            elif choice.find("read") != -1 or choice == "2":       # if user select read
                self.read_from_text_file_menu()                                  # open menu to read news
            elif choice.find("json") != -1 or choice == '3':        # if user select read from JSON file
                self.read_from_json_file_menu()                         # open menu to read JSON
            elif choice.find("xml") != -1 or choice == '4':        # if user select read from JSON file
                self.read_from_xml_file_menu()                         # open menu to read JSON
            elif choice.find("exit") != -1 or choice == "0":       # if user select exit
                break                                                       # exit from the loop
            else:                                                           # if input was not recognized - try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'generate\', "
                      "\'read\' or \'exit\'")
        self.db.cursor.close()              # close db cursor
        self.db.connection.close()          # close db connection

    # function with general menu
    def generate_news_menu(self):
        while True:
            print("Select data type to generate: \n"  # print menu text 
                  "\t1. News\n"  # to generate news
                  "\t2. Private ad\n"  # to generate ad 
                  "\t3. Weather forecast for tomorrow\n"  # to generate weather forecast
                  "\t0. Back")  # to exit from the loop

            choice = NewsGeneratorMenu.get_input_from_console()     # get input from the console

            if choice.find("news") != -1 or choice == "1":  # if user selected news or menu number
                # FileOperations(add_news_menu())  # write to file generated news feed
                self.news_feeds_menu()  # Call the function to get news generator menu
                # if user selected ad, private of menu number
            else:
                if choice.find("ad") != -1 or choice.find("private") != -1 or choice == "2":
                    self.private_ad_menu()  # Call the function to get private ad generator menu
                else:
                    # if user selected weather or menu number
                    if choice.find("weather") != -1 or choice == "3":
                        self.weather_forecast_menu()  # Call the function to get weather forecast generator menu
                    else:
                        # if user selected exit of menu number
                        if choice.find("back") != -1 or choice == "0":
                            break  # exit from the infinite loop
                        else:  # else print to console that printed text was incorrect
                            print("Incorrect data type selected. Try again to type menu number (0-3) or type \'news\', "
                                  "\'ad\' or \'weather\'")

    # menu function to define input source for file to read
    def read_from_text_file_menu(self):
        while True:     # loop until exit
            print("Read from the default file or select another file?:\n"
                  "\t1. Default file\n"
                  "\t2. Personal file\n"
                  "\t0. Back")
            choice = NewsGeneratorMenu.get_input_from_console()            # get input from the console
            if choice.find("default") != -1 or choice == "1":     # if user select default file
                self.get_records_from_default_file()                          # open default file
            elif choice.find("personal") != -1 or choice == "2":  # if user select personal file
                self.get_records_from_personal_file()                         # open personal file
            elif choice.find("back") != -1 or choice == "0":      # if user select back
                break                                                      # go to previous menu
            else:                                                          # if input was not recognized - try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'default\', "
                      "\'personal\' or \'back\'")

    # function to select input json file to read
    def read_from_json_file_menu(self):
        while True:     # infinite loop until break
            print("Read from the default file or select another file?:\n"   # print menu
                  "\t1. Default file\n" 
                  "\t2. Personal file\n"
                  "\t0. Back")
            choice = NewsGeneratorMenu.get_input_from_console()  # get input from the console
            if choice.find("default") != -1 or choice == "1":   # if user select default file
                self.get_records_from_default_json_file()       # call the function to write records to default file
            elif choice.find("personal") != -1 or choice == "2":    # if user select personal file
                self.get_records_from_personal_json_file()      # call the function to write to personal file
            elif choice == "back" or choice == "0":         # exit to previous menu
                break
            else:                                           # else try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'default\', "
                      "\'personal\' or \'back\'")

        # function to select input json file to read

    def read_from_xml_file_menu(self):
        while True:  # infinite loop until break
            print("Read from the default file or select another file?:\n"  # print menu
                  "\t1. Default file\n"
                  "\t2. Personal file\n"
                  "\t0. Back")
            choice = NewsGeneratorMenu.get_input_from_console()  # get input from the console
            if choice.find("default") != -1 or choice == "1":  # if user select default file
                self.get_records_from_default_xml_file()  # call the function to write records to default file
            elif choice.find("personal") != -1 or choice == "2":  # if user select personal file
                self.get_records_from_personal_xml_file()  # call the function to write to personal file
            elif choice == "back" or choice == "0":  # exit to previous menu
                break
            else:  # else try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'default\', "
                      "\'personal\' or \'back\'")

    # function to generate news record
    def news_feeds_menu(self):
        news_body = input("What's happen? \n")  # input from the console text of the news feed
        if len(news_body) == 0:  # put input was empty
            # print default text for news feed
            news_body = "Something happen"
        news_city_timestamp = input("Where something happen? \n")  # input from the console city of the news
        if len(news_city_timestamp) == 0:  # if input was empty
            news_city_timestamp = "Somewhere"  # put default value as a city
        # adding timestamp string city timestamp
        news_city_timestamp += datetime.now().strftime(", %Y-%m-%d %H:%M")
        # initialization of the News object with provided text, city and timestamp
        news = News(news_body, news_city_timestamp)
        self.db.write_obj_to_db(news)            # write object to db
        # write generated news object to file
        self.file_to_write.write_to_file(news.convert_to_string())

    # function to generate private ad record
    def private_ad_menu(self):
        ad_text = input('What you would like to advertise? \n')  # input from the console text of the private ad
        if len(ad_text) == 0:  # if input value is empty
            ad_text = 'Buy an elephant!'  # put default value to the variable
        while True:  # infinite loop to get correct expiration date
            # input the date from the console
            ad_expiration_date = input("What is an expiration date of this advertisement? ( in yyyy-mm-dd format) \n")
            if len(ad_expiration_date) == 0:  # if input is empty
                ad_expiration_date = datetime.now().date() + timedelta(days=7)  # put the default value
                break       # break the loop
            else:  # if input is not empty
                try:  # error handler of incorrect input data
                    # initialization of the expiration date in proper format
                    ad_expiration_date = datetime.strptime(str(ad_expiration_date), '%Y-%m-%d').date()
                    if ad_expiration_date < datetime.now().date():  # if input date is less than current one
                        print("Entered expiration date is less than current one. Please try again.")  # print to console
                    else:  # if input date is more than current one
                        break  # exit from the loop
                except ValueError:  # exception handler
                    print("Entered expiration date has wrong format. Please, try again.")  # print to console
        # write generated private ad to file
        # self.file_to_write.write_to_file(PrivateAd().generate_private_ad(ad_text, ad_expiration_date))
        # initialization of the PrivateAd object with advertisement text and expiration date
        ads = PrivateAd(ad_text, ad_expiration_date)
        self.db.write_obj_to_db(ads)               # write object to db
        self.file_to_write.write_to_file(ads.convert_to_string())  # write generated record to the file

    # function to generate weather forecast
    def weather_forecast_menu(self):
        weather_details = input('Specify weather details \n')   # input from the console
        if not len(weather_details):                            # put default value if input was empty
            weather_details = 'It would be a great day!'
        location_for_weather = input('For what city you would like to get weather forecast? \n')    # input location
        if not len(location_for_weather):  # if input value is empty
            location_for_weather = 'Krakow'  # put default value to the variable
        # initialization of the WeatherForecast object with weather text and city
        weather = WeatherForecast(weather_details, location_for_weather)
        self.db.write_obj_to_db(weather)         # write object to db
        self.file_to_write.write_to_file(weather.convert_to_string())  # write generated weather forecast to file

    # function to get records from default file
    @staticmethod
    def get_records_from_default_file():
        file_to_read = RecordsFromFilesHandler()      # initialization object of the RecordsFromFilesHandler class
        file_to_read.write_new_records_to_the_file()  # write new records to the file

    # function to get records from provided file
    @staticmethod
    def get_records_from_personal_file():
        # initialization object of the RecordsFromFilesHandler class with provided path
        file_to_read = RecordsFromFilesHandler(FileOperations.get_file_path('.txt'))
        file_to_read.write_new_records_to_the_file()  # write new records to the file

    # function to write records from default json file
    @staticmethod
    def get_records_from_default_json_file():
        if FileOperations.is_file_exist(default_file_path_to_json_file):
            json_operations = JsonManager()     # initialization of JsonManager class object
            json_operations.write_unique_records_to_file()  # function to write unique records, file path = default
        else:
            print("Default file doesn't exist")

    # function to write records from json file with providing file path
    @staticmethod
    def get_records_from_personal_json_file():
        file_path = FileOperations.get_file_path('.json')   # defining file path from the console
        if FileOperations.is_file_exist(file_path):
            json_operations = JsonManager()  # initialization of JsonManager class object
            json_operations.file_path = file_path
            json_operations.write_unique_records_to_file()  # call the function to write records with defined file path
        else:
            print("Provided file doesn't exist")

    @staticmethod
    def get_records_from_default_xml_file():
        if FileOperations.is_file_exist(default_file_path_to_xml_file):
            xml_operations = XMLManager()     # initialization of XMLManager class object
            xml_operations.write_unique_records_to_file()  # function to write unique records, file path = default
        else:
            print("Default file doesn't exist")

    @staticmethod
    def get_records_from_personal_xml_file():
        file_path = FileOperations.get_file_path('.xml')  # defining file path from the console
        if FileOperations.is_file_exist(file_path):
            xml_operations = XMLManager(file_path)  # initialization of XMLManager class object
            xml_operations.write_unique_records_to_file()  # call the function to write records with defined file path
        else:
            print("Provided file doesn't exist")
