import logging
import os

class LogGen:
    @staticmethod
    def loggGenaration():

        path = os.path.abspath(os.curdir)+'\\logs\\automation.log'
        # path = os.getcwd()+ '\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

