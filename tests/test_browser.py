from unittest.mock import MagicMock, patch

import pytest
from selenium.webdriver import Chrome

from harlow_bindicator.app.browser import Browser
from harlow_bindicator.app.configuration import Configuration


def test_construtor():
    with pytest.raises(Exception):
        Browser()


def test_constructor_with_configuration():
    config = Configuration()
    browser = Browser(config, "test_url")
    assert browser.configuration == config
    assert browser.url == "test_url"


@patch("harlow_bindicator.app.browser.webdriver")
def test_get_data(web_driver):
    config = Configuration()
    browser = Browser(config, "test_url")
    chrome = MagicMock(spec=Chrome)
    web_driver.Chrome.return_value = chrome
    chrome.page_source = "page_data"
    source = browser.get_web_page()

    assert source == "page_data"
    chrome.get.assert_called_once_with("test_url00000000001")


@patch("harlow_bindicator.app.browser.webdriver")
def test_get_data_simple_mocks(web_driver):
    config = Configuration()
    browser = Browser(config, "test_url")
    web_driver.Chrome().page_source = "page_data"
    source = browser.get_web_page()

    assert source == "page_data"
    web_driver.Chrome().get.assert_called_once_with("test_url00000000001")
