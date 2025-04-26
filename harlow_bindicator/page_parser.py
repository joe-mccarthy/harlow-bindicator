import logging
from datetime import datetime
from typing import List

import bs4

from .data import Collection, CollectionDate


class Parser:

    def parse(self, page_source: str) -> List[CollectionDate]:

        soup = bs4.BeautifulSoup(page_source, "html.parser")
        collections = soup.find_all(attrs={"class": ["collectionsrow"]})
        collections.pop(0)

        logging.info("Parsing html page for bin collection data")

        collection_data = []
        for collection in collections:
            children = collection.find_all("div", recursive=False)
            children.pop(0)
            bin_type = self.__get_type(children[0].contents)
            bin_date = self.__get_date(children[1].contents)
            collection_data.append(Collection(bin_type, bin_date))

        filtered = [
            collection_data[i : i + 2] for i in range(0, len(collection_data), 2)
        ]

        day_data = []

        for data in filtered:
            day_data.append(CollectionDate(data[1]))

        return day_data

    def __get_type(self, data) -> str:
        return data[0]

    def __get_date(self, data) -> str:
        raw_date = data[0].split("- ", 1)[1]
        return datetime.strptime(raw_date, "%d %b %Y").strftime("%d/%m/%Y")
