from unittest.mock import patch

import pytest
from datetime import date, timedelta


from harlow_bindicator.bindicator import Bindicator
from harlow_bindicator.data import Collection, CollectionDate


def test_bindicator_init():
    with pytest.raises(TypeError):
        Bindicator()


@patch("harlow_bindicator.bindicator.Api")
def test_bindicator_run_no_collections(mock_api):
    bindicator = Bindicator("uprn", "topic")
    mock_api().get_data.return_value = None
    bindicator.run()
    mock_api().get_data.assert_called_once()


@patch("harlow_bindicator.bindicator.Api")
@patch("harlow_bindicator.bindicator.requests")
def test_bindicator_run_collections(mock_requests, mock_api):
    bindicator = Bindicator("uprn", "topic")
    today = date.today()
    collection = Collection("recycling", today.strftime("%d/%m/%Y"))
    collection_date = CollectionDate(collection)
    mock_api().get_data.return_value = [collection_date]

    bindicator.run()

    mock_api().get_data.assert_called_once()
    mock_requests.post.assert_called_once_with(
        "https://ntfy.sh/topic",
        data=f"Bin collection is today for {collection_date.wheelie.bin_type}".encode(
            encoding="utf-8",
        ),
        headers={
            "Title": "Binday Today",
            "Priority": "3",
            "Tags": "rotating_light",
        },
    )


@patch("harlow_bindicator.bindicator.Api")
@patch("harlow_bindicator.bindicator.requests")
def test_bincollection_tomorrow(mock_requests, mock_api):
    bindicator = Bindicator("uprn", "topic")
    today = date.today()
    collection = Collection(
        "recycling", (today + timedelta(days=1)).strftime("%d/%m/%Y")
    )
    collection_date = CollectionDate(collection)
    mock_api().get_data.return_value = [collection_date]

    bindicator.run()

    mock_api().get_data.assert_called_once()
    mock_requests.post.assert_called_once_with(
        "https://ntfy.sh/topic",
        data=f"Bin collection is tomorrow for {collection_date.wheelie.bin_type}".encode(
            encoding="utf-8",
        ),
        headers={
            "Title": "Binday Tomorrow",
            "Priority": "3",
            "Tags": "warning",
        },
    )


@patch("harlow_bindicator.bindicator.Api")
@patch("harlow_bindicator.bindicator.requests")
def test_no_collection_today(mock_requests, mock_api):
    bindicator = Bindicator("uprn", "topic")

    future_date = (date.today() + timedelta(days=2)).strftime("%d/%m/%Y")
    collection = Collection("recycling", future_date)
    collection_date = CollectionDate(collection)
    mock_api().get_data.return_value = [collection_date]

    bindicator.run()

    mock_api().get_data.assert_called_once()
    mock_requests.post.assert_not_called()
