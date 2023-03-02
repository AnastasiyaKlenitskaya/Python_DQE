from datetime import datetime


class News:

    def __init__(self):
        self.news_in_string = 'News -------------------------\n'    # initialization of the local variable

    def generate_news_feed(self, news_body: str, news_city: str) -> str:
        timestamp = datetime.now()  # initialization of the variable with current timestamp
        current_time = str(timestamp.time()).split(':')  # initialization of the variable with string of current time
        current_time = str(
            current_time[0] + ':' + current_time[1])  # put hour and minute value to the variable current time
        # complete string that will be written to file
        self.news_in_string += str(news_body + '\n' + news_city + ', ' + str(timestamp.day) + '-' + str(timestamp.month)
                                   + '-' + str(
            timestamp.year) + ' ' + current_time + '\n------------------------------\n\n')
        return self.news_in_string      # return generated news as a string
