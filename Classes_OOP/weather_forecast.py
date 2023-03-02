import random


class WeatherForecast:

    list_of_possible_weathers = ['Sunny', 'Cloudy', 'Flood', 'Fog', 'Hail', 'Ice', 'Lightning', 'Thunder', 'Windy']

    def __init__(self):
        self.weather_forecast_in_string = 'Weather forecast -------------\n'

    def generate_weather_forecast(self, location_for_weather: str) -> str:
        self.weather_forecast_in_string += 'Weather for ' + location_for_weather + ':\nTemperature is ' \
                                           + str(random.randint(-20, + 35)) + ', ' \
                                           + self.list_of_possible_weathers[random.randint(0, len(self.list_of_possible_weathers) - 1)] \
                                           + '.\n------------------------------\n\n'

        return self.weather_forecast_in_string
