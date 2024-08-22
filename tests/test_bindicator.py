from unittest.mock import patch

import pytest

from harlow_bindicator.app.bindicator import Bindicator
from harlow_bindicator.app.configuration import Configuration
from harlow_bindicator.app.data import Collection, CollectionDate


def test_bindicator_init():
    with pytest.raises(Exception):
        Bindicator()


@patch("harlow_bindicator.app.bindicator.MQTT")
def test_bindicator_init_config(mock_mqtt):
    config = Configuration()
    bindicator = Bindicator(config)

    assert bindicator
    assert bindicator.configuration
    assert bindicator.mqtt_client
    assert bindicator.api
    mock_mqtt.called_once_with(config)


@patch("harlow_bindicator.app.bindicator.MQTT")
@patch("harlow_bindicator.app.bindicator.Api")
def test_bindicator_run_no_collections(mock_api, mock_mqtt):
    config = Configuration()
    bindicator = Bindicator(config)

    mock_api().get_data.return_value = None

    bindicator.run()

    mock_api().get_data.called_once()
    assert not mock_mqtt().publish.called


@patch("harlow_bindicator.app.bindicator.MQTT")
@patch("harlow_bindicator.app.bindicator.Api")
def test_bindicator_run_collections(mock_api, mock_mqtt):
    config = Configuration()
    bindicator = Bindicator(config)

    collection = Collection("recycling", "15/1/2023")
    collection_date = CollectionDate(collection)
    mock_api().get_data.return_value = [collection_date]
    expected = '{"date": "15/01/2023", "bin_day": false, "bin_type": "recycling"}'

    bindicator.run()

    mock_api().get_data.called_once()
    mock_mqtt().publish.called_once_with(expected)
