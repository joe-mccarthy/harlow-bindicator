from unittest.mock import MagicMock, patch

import pytest
from selenium.webdriver import Chrome

from src.app.browser import Browser


def test_constructor():
    with pytest.raises(Exception):
        Browser()


def test_constructor_with_configuration():
    browser = Browser("123456", "test_url")
    assert browser.uprn == "123456"
    assert browser.url == "test_url"


@patch("src.app.browser.webdriver")
def test_get_data(web_driver):
    browser = Browser("123456", "test_url")
    chrome = MagicMock(spec=Chrome)
    web_driver.Chrome.return_value = chrome
    chrome.page_source = "page_data"
    source = browser.get_web_page()

    assert source == "page_data"
    chrome.get.assert_called_once_with("test_url123456")


@patch("src.app.browser.webdriver")
def test_get_data_simple_mocks(web_driver):
    browser = Browser("123456", "test_url")
    web_driver.Chrome().page_source = "page_data"
    source = browser.get_web_page()

    assert source == "page_data"
    web_driver.Chrome().get.assert_called_once_with("test_url123456")
