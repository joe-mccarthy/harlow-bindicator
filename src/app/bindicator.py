import logging

from .api import Api
from datetime import date, timedelta
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
                f"{len(collections)} found publishing first collection date information"
            )
            today = date.today()
            tomorrow = today + timedelta(days=1)
            collection_date = collections[0].date
            bin_type = collections[0].wheelie.bin_type
            if today == collection_date:
                message = f"Bin collection is today for {bin_type}"
                logging.info(message)
                logging.info("Publishing message to ntfy.sh")
                requests.post(
                    f"https://ntfy.sh/{self.topic}",
                    data=message.encode(encoding="utf-8"),
                    headers={
                        "Title": "Binday Today",
                        "Priority": "3",
                        "Tags": "rotating_light",
                    },
                )
            elif tomorrow == collection_date:
                message = f"Bin collection is tomorrow for {bin_type}"
                logging.info(message)
                logging.info("Publishing message to ntfy.sh")
                requests.post(
                    f"https://ntfy.sh/{self.topic}",
                    data=message.encode(encoding="utf-8"),
                    headers={
                        "Title": "Binday Tomorrow",
                        "Priority": "3",
                        "Tags": "warning",
                    },
                )
            else:
                logging.info("No bin collection today")
                logging.info(f"Next bin collection is {collection_date}, {bin_type}")
