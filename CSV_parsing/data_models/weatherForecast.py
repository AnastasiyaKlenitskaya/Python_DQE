from random import randint
from data_models.record import Record
from config import title_length

# class inherits Record class and initialize a WeatherForecast object with record text
class WeatherForecast(Record):
    # list of possible weathers
    list_of_possible_weathers = ['Sunny', 'Cloudy', 'Flood', 'Fog', 'Hail', 'Ice', 'Lightning', 'Thunder', 'Windy']

    # class constructor, get text and location as arguments
    def __init__(self, text, location):
        self.title = 'Weather Forecast ' + '-' * (title_length - len('Weather Forecast '))   # generate tite
        super().__init__(self.title, text)   # super class constructor call
        # generate location text
        self.location = 'Weather for ' + location + ':\nTemperature is ' \
                        + str(randint(-20, + 35)) + ', ' \
                        + self.list_of_possible_weathers[randint(0, len(self.list_of_possible_weathers) - 1)]
