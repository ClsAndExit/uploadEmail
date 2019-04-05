import logging


def get_logger_by_name(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(filename=name+".log")
    logger.setLevel(logging.INFO)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(filename)s:%(levelname)s:%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
