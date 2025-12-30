import logging

class Log_Genrater_Class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger(__name__)
        logfile = logging.FileHandler(r"D:\pro\CredKartFreamwork\Logs\CredKart.log")
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.DEBUG)
        return logger


