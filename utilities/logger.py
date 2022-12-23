import inspect
import logging


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)  # or use __name__ (default) that returns package/module name
    filehandler = logging.FileHandler('test_logs.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)  # set level FROM which the logs will be passed to handler
    return logger
