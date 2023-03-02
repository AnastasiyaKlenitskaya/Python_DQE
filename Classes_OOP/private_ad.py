from datetime import datetime, date


class PrivateAd:

    def __init__(self):
        self.private_ad_text = 'Private Ad -------------------\n'

    def generate_private_ad(self, ad_body_text: str, ad_expiration_date: date) -> str:
        self.private_ad_text = 'Private Ad ------------------\n'
        self.private_ad_text += ad_body_text + '\nActual until: ' + str(ad_expiration_date) + ' '\
                       + str((ad_expiration_date - datetime.now().date()).days) \
                       + ' days left \n------------------------------\n\n'
        return self.private_ad_text
