from unittest.mock import patch

from harlow_bindicator.api import Api


def test_init():
    api = Api(uprn="123456789")
    assert api.uprn == "123456789"


@patch("harlow_bindicator.api.Parser")
@patch("harlow_bindicator.api.Browser")
def test_browser_and_parser_called(mock_browser, mock_parser):
    api = Api(uprn="123456789")
    mock_browser().get_web_page.return_value = "page_source"
    mock_parser().parse.return_value = ["data"]

    assert api.get_data()[0] == "data"
    mock_browser().get_web_page.assert_called_once()
    mock_parser().parse.assert_called_once_with("page_source")
