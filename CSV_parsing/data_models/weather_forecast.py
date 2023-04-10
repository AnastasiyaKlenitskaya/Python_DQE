from random import randint
from CSV_parsing.data_models.record import Record


# class inherits Record class and initialize a WeatherForecast object with record text
class WeatherForecast(Record):
    # list of possible weathers
    list_of_possible_weathers = ['Sunny', 'Cloudy', 'Flood', 'Fog', 'Hail', 'Ice', 'Lightning', 'Thunder', 'Windy']

    # class constructor, get text and location as arguments
    def __init__(self, text, location):
        self.title = Record.generate_header('Weather Forecast ')    # generate tite
        super().__init__(self.title, text)   # super class constructor call
        # generate location text
        self.location = 'Weather for ' + location + ': temperature is ' \
                        + str(randint(-20, + 35)) + ', ' \
                        + self.list_of_possible_weathers[randint(0, len(self.list_of_possible_weathers) - 1)]
