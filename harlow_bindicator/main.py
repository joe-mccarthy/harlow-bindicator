import logging
import argparse

from .bindicator import Bindicator


def fetch_bin_collection():

    logging.basicConfig(
        level="INFO",
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info("Creating Harlow Bindicator")
    parser = argparse.ArgumentParser(description="Environment Checker")
    parser.add_argument(
        "--uprn", type=str, required=True, help="Property Reference Number"
    )
    parser.add_argument("--topic", type=str, required=True, help="Ntfy Topic")
    args = parser.parse_args()    
    bindicator = Bindicator(args.uprn, args.topic)
    bindicator.run()
    logging.info("Harlow Bindicator run completed")
