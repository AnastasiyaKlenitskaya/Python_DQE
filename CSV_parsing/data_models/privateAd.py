from datetime import datetime
from config import title_length
from data_models.record import Record

# class inherits Record class and initialize a PrivateAd object with record text
class PrivateAd(Record):

    # class constructor, get text and expiration date
    def __init__(self, text, ad_expiration_date):
        self.title = 'Private ad ' + '-' * (title_length - len('Private ad '))  # generate tite
        super().__init__(self.title, text)      # super class constructor call
        # generating expiration date text
        self.ad_expiration_date = 'Actual until: ' + str(ad_expiration_date) + ', ' \
                                  + str((ad_expiration_date - datetime.now().date()).days) \
                                  + ' days left'
