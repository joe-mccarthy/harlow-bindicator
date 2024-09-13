import logging

from .api import Api
from datetime import date
import requests

class Bindicator:

    api: Api

    def __init__(self, uprn, topic) -> None:
        self.api = Api(uprn)
        self.topic = topic

    def run(self):
        collections = self.api.get_data()

        if collections:
            logging.debug(
                f'{len(collections)} found publishing first collection date information')
            if date.today() == collections[0].date:
                message =  f'Bin collection is today for {collections[0].wheelie.bin_type}'
                logging.info(message                   )
                requests.post(f"https://ntfy.sh/{self.topic}",data=message.encode(encoding='utf-8'))
            else:
                logging.info(
                    f'Next bin collection is {collections[0].date}, {collections[0].wheelie.bin_type}')