import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)