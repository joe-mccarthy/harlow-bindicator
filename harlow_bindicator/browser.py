import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Browser:

    def __init__(self, uprn, url: str) -> None:
        self.url = url
        self.uprn = uprn

    def get_web_page(self) -> str:
        data_url = f"{self.url}{self.uprn}"

        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]
        for option in options:
            chrome_options.add_argument(option)

        logging.debug(options)

        executable_path = "/usr/bin/chromedriver"
        chrome_service = Service(executable_path)

        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        logging.info("Retrieving bin collection webpage")
        driver.get(data_url)
        return driver.page_source
