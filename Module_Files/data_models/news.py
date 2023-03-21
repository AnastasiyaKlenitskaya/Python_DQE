from config import title_length
from data_models.record import Record

# class inherits Record class and initialize a News object with record text
class News(Record):

    # class constructor, get text and city_timestamp as arguments
    def __init__(self, text, city_timestamp):
        self.title = 'News ' + '-' * (title_length - len('News '))  # generates title
        self.city_timestamp = city_timestamp    # initialize self city_timestamp
        super().__init__(self.title, text)  # super class constructor call
