from unittest.mock import patch

from harlow_bindicator.app.configuration import Configuration
from harlow_bindicator.app.mqtt import MQTT


@patch('harlow_bindicator.app.mqtt.paho')
def test_connection(mock_paho):
    config = Configuration()
    MQTT(config)
    mock_paho.Client.called_once_with("bindicator_client")
    mock_paho.Client.connect.called_once_with("broker")


@patch('harlow_bindicator.app.mqtt.paho')
def test_publish_message(mock_paho):
    config = Configuration()
    mqtt = MQTT(config)
    mqtt.publish("test message")
    mock_paho.publish.called_once_with("bindicator", "test_message")
