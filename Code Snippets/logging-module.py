import logging, datetime

get_date = datetime.datetime.now().strftime("%Y%m%d_%H%M")

logging.basicConfig(level=logging.INFO, filename=f"{get_date}-log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("An error has occurred")
logging.critical("critical")

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("Zero")