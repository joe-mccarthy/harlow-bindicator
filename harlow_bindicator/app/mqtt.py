import logging

import paho.mqtt.client as paho

from .configuration import Configuration


class MQTT:

    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration
        logging.debug(
            f'Creating MQTT client with ID:{self.configuration.mqtt_client_id}')
        self.mqtt_client = paho.Client(
            client_id=self.configuration.mqtt_client_id)
        logging.debug(
            f'Attempting connection to MQTT broker {self.configuration.mqtt_addresss}')
        self.mqtt_client.connect(self.configuration.mqtt_addresss)
        logging.info('Connected to MQTT Broker')

    def publish(self, message: str):
        logging.debug(
            f'Publishing message {message} to {self.configuration.mqtt_topic} on broker {self.configuration.mqtt_addresss}')
        self.mqtt_client.publish(self.configuration.mqtt_topic, message)
        logging.info('Published message to MQTT Broker')
