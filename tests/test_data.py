from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from src.app.data import Collection, CollectionDate


def test_collection_date_parse():
    date = datetime(2023, 1, 15).date()
    collection = Collection("recycling", "15/1/2023")
    assert collection
    assert collection.bin_type == "recycling"
    assert collection.date == date


def test_collection_init():
    with pytest.raises(Exception):
        Collection()


def test_collection_date_init():
    with pytest.raises(Exception):
        CollectionDate()


def test_collection_date():
    date = datetime(2023, 1, 15).date()
    collection = Collection("recycling", "15/1/2023")
    collection_date = CollectionDate(collection)
    assert collection_date
    assert collection_date.wheelie.bin_type == "recycling"
    assert collection_date.date == date


@patch("src.app.data.datetime")
def test_is_binday_true(mock_datetime):
    collection = MagicMock()
    collection.date = datetime(2023, 1, 15).date()
    collection_date = CollectionDate(collection)
    mock_datetime.now.return_value = datetime(2023, 1, 15)
    assert collection_date.is_bin_day()


def test_collection_date_create_message():
    collection = Collection("recycling", "15/1/2023")
    collection_date = CollectionDate(collection)
    message = collection_date.create_message()
    expected = '{"date": "15/01/2023", "bin_day": false, "bin_type": "recycling"}'
    assert message == expected
