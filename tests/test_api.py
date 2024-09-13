from unittest.mock import patch

from src.app.api import Api


def test_init():
    api = Api(uprn="123456789")
    assert api.uprn == "123456789"


@patch("src.app.api.Parser")
@patch("src.app.api.Browser")
def test_browser_and_parser_called(mock_browser, mock_parser):
    api = Api(uprn="123456789")
    mock_browser().get_web_page.return_value = "page_source"
    mock_parser().parse.return_value = ["data"]

    assert api.get_data()[0] == "data"
    mock_browser.get_web_page.called_once()
    mock_parser.parse.called_once_with("page_source")
