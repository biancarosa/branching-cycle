import logging

LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
              "-30s %(funcName) -35s %(lineno) -5d: %(message)s")

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def getLogger(owner):
    logger = logging.getLogger(owner)
    return logger
