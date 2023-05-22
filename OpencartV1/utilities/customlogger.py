import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.pth.abspath(os.curdiur) + ".\\logs\\automation.log"
        logging.basicConfig(filename=path,
                            format="%(asctime)s: %(levelname)s: %(message)s" ,
                            datefmt="%m/%d/%Y %I:%M:%S %P")
        logger = logging.getLogger()
        logger.setlevel(logging.DEBUG)
        return logger