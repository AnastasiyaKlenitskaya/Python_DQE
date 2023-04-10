from datetime import datetime
from CSV_parsing.data_models.record import Record

# class inherits Record class and initialize a PrivateAd object with record text
class PrivateAd(Record):

    # class constructor, get text and expiration date
    def __init__(self, text: str, ad_expiration_date):
        self.title = Record.generate_header('Private ad ')  # generate tite
        super().__init__(self.title, text)      # super class constructor call
        # generating expiration date text
        self.ad_expiration_date = 'Actual until: ' + str(ad_expiration_date) + ', ' \
                                  + str((ad_expiration_date - datetime.now().date()).days) \
                                  + ' days left'
