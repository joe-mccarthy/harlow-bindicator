import logging

from .api import Api
from .configuration import Configuration
from .mqtt import MQTT


class Bindicator:

    api: Api
    configuration: Configuration

    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration
        self.mqtt_client = MQTT(self.configuration)
        self.api = Api(self.configuration)

    def run(self):
        logging.info('Running Harlow Bindicator')
        logging.debug(f'Property for bin collection {self.configuration.uprn}')
        collections = self.api.get_data()

        if collections:
            logging.debug(
                f'{len(collections)} found publishing first collection date information')
            self.mqtt_client.publish(collections[0].create_message())
