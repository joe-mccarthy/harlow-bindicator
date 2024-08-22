import logging
import time

from app.bindicator import Bindicator
from app.configuration import Configuration

if __name__ == "__main__":

    configuration = Configuration()

    logging.basicConfig(
        level=configuration.logging_level,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.debug(
        f'Parsed configuraiton and set logging to {configuration.logging_level}')

    while True:
        logging.info('Creating Harlow Bindicator')
        bindicator = Bindicator(configuration)
        bindicator.run()
        logging.info('Harlow Bindicator run completed')
        logging.info(f'Sleeping for {configuration.pause_minutes} minutes')
        time.sleep(60 * configuration.pause_minutes)
