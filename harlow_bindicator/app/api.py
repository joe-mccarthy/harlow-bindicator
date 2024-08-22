from typing import List

from .browser import Browser
from .configuration import Configuration
from .data import CollectionDate
from .page_parser import Parser


class Api:

    url: str = "https://selfserve.harlow.gov.uk/appshost/firmstep/self/apps/custompage/bincollectionsecho?uprn="

    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration
        self.browser = Browser(configuration, self.url)

    def get_data(self) -> List[CollectionDate]:
        page_source = self.browser.get_web_page()
        parser = Parser()
        return parser.parse(page_source)
