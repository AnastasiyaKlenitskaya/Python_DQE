from FileOperations import FileOperations
from news import News
from weather_forecast import WeatherForecast
from private_ad import PrivateAd
from datetime import datetime
from datetime import timedelta


class NewsGeneratorMenu:

    def __init__(self):
        self.file = FileOperations()        # initialization of local variable with object of FileOperations class

    # function with general menu
    def general_menu(self):
        while True:
            print("Select data type to generate: \n"  # print menu text 
                  "\t1. News\n"  # to generate news
                  "\t2. Private ad\n"  # to generate ad 
                  "\t3. Weather forecast for tomorrow\n"  # to generate weather forecast
                  "\t0. Exit")  # to exip from the loop

            menu_input = input("Your choice: ")  # input selected option from the console
            menu_input = menu_input.lower()  # lowercased input text

            if menu_input.find("news") != -1 or menu_input.find("1") != -1:  # if user selected news or menu number
                # FileOperations(add_news_menu())  # write to file generated news feed
                self.news_feeds_menu()      # Call the function to get news generator menu
            else:
                # if user selected ad, private of menu number
                if menu_input.find("ad") != -1 or menu_input.find("private") != -1 or menu_input.find("2") != -1:
                    self.private_ad_menu()      # Call the function to get private ad generator menu
                else:
                    # if user selected weather or menu number
                    if menu_input.find("weather") != -1 or menu_input.find("3") != -1:
                        self.weather_forecast_menu()    # Call the function to get weather forecast generator menu
                    else:
                        # if user selected exit of menu number
                        if menu_input.find("exit") != -1 or menu_input.find("0") != -1:
                            break  # exit from the infinite loop
                        else:  # else print to console that printed text was incorrect
                            print("Incorrect data type selected. Try again to type menu number (1-3) or type \'news\', "
                                  "\'ad\' or \'weather\'")

    def news_feeds_menu(self):
        news_body = input("What's happen? \n")  # input from the console text of the news feed
        if len(news_body) == 0:  # put input was empty
            # print default text for news feed
            news_body = "Something happen. Right now we don't understands what exactly. But something absolutely happen"
        news_city = input("Where something happen? \n")  # input from the console city of the news
        if len(news_city) == 0:  # if input was empty
            news_city = "Somewhere. Yes, just somewhere"  # put default value as a city
        # write generated news to file
        self.file.write_to_file(News().generate_news_feed(news_body, news_city))
        pass

    def private_ad_menu(self):
        ad_text = input('What you would like to advertise? \n')  # input from the console text of the private ad
        if len(ad_text) == 0:  # if input value is empty
            ad_text = 'Buy an elephant!'  # put default value to the variable
        while True:  # infinite loop to get correct expiration date
            # input the date from the console
            ad_expiration_date = input("What is an expiration date of this advertisement? ( in dd/mm/yyyy format) \n")
            if len(ad_expiration_date) == 0:  # if input is empty
                ad_expiration_date = datetime.now().date() + timedelta(days=7)  # put the default value
                break
            else:  # if input is not empty
                try:  # error handler of incorrect input data
                    # converting input value to the date format
                    ad_expiration_date = datetime.strptime(str(ad_expiration_date), '%d/%m/%Y').date()
                    if ad_expiration_date < datetime.now().date():  # if input date is less than current one
                        print("Entered expiration date is less than current one. Please try again.")  # print to console
                    else:  # if input date is more than current one
                        break  # exit from the loop
                except ValueError:  # exception handler
                    print("Entered expiration date has wrong format. Please, try again.")  # print to console
        # write generated private ad to file
        self.file.write_to_file(PrivateAd().generate_private_ad(ad_text, ad_expiration_date))
        pass

    def weather_forecast_menu(self):
        location_for_weather = input('For what city you would like to get weather forecast? \n')
        if len(location_for_weather) == 0:  # if input value is empty
            location_for_weather = 'Krakow'  # put default value to the variable
        # write generated weather forecast to file
        self.file.write_to_file(WeatherForecast().generate_weather_forecast(location_for_weather))
        pass
