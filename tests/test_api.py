from unittest.mock import patch

from harlow_bindicator.app.api import Api
from harlow_bindicator.app.configuration import Configuration


def test_init():
    config = Configuration()
    api = Api(config)
    assert api.configuration


@patch("harlow_bindicator.app.api.Parser")
@patch("harlow_bindicator.app.api.Browser")
def test_browser_and_parser_called(mock_browser, mock_parser):
    config = Configuration()
    api = Api(config)
    mock_browser().get_web_page.return_value = "page_source"
    mock_parser().parse.return_value = ["data"]

    assert api.get_data()[0] == "data"
    mock_browser.get_web_page.called_once()
    mock_parser.parse.called_once_with("page_source")
