import json
from datetime import datetime


class Collection:

    def __init__(self, type, date) -> None:
        self.bin_type = type
        self.date = datetime.strptime(date, "%d/%m/%Y").date()


class CollectionDate:

    def __init__(self, wheelie: Collection) -> None:
        self.wheelie = wheelie
        self.date = wheelie.date

    def is_bin_day(self) -> bool:
        return self.date == datetime.now().date()

    def create_message(self) -> str:
        payload = json.dumps(
            {
                "date": self.date.strftime("%d/%m/%Y"),
                "bin_day": self.is_bin_day(),
                "bin_type": self.wheelie.bin_type,
            }
        )
        return payload
