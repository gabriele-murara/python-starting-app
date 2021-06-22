import logging
import logging.config
import importlib
from settings import constants
import mysql.connector

class Configuration():

    def __init__(self, config_file):
        self._dict = {}
        self._config_file = config_file
        self._init_configuration()
        self.logger.debug(
            "Created {} Configuration".format(constants.__app_alias__)
        )

    def _init_configuration(self):
        self._init_configuration_file()
        self._init_logger()
        self._init_db_connection()

    def _init_configuration_file(self):
        module_name = "settings.{}".format(self._config_file)
        self._dict = importlib.import_module(module_name)

    def _init_logger(self):
        module_name = "settings.{}".format(self._config_file)
        try:
            logging.config.dictConfig(
                importlib.import_module(module_name).LOGGING
            )
        except ModuleNotFoundError as me:
            msg = "Module '{}' not found. Kill the process with code 1."
            print(msg.format(module_name))
            exit(1)

        logger = logging.getLogger('base')
        logger.setLevel(logging.DEBUG)
        msg = "Loaded configuration module '{}'".format(module_name)
        logger.info(msg)
        msg = "Starting {} v. {}".format(
            constants.__app_alias__, constants.__version__
        )

        try:
            logger.debug(msg)
        except Exception as e:
            msg = "Something goes wrong with logging. Details ({})".format(e)
            print(msg)
            print("Kill the process with code 2")
            exit(2)
        self.logger = logger

    def _init_db_connection(self):
        try:
            cnx = self._get_db_connection();
            cnx.close()
            msg = "Database inited"
            self.logger.info(msg)
        except Exception as e:
            print(e)
            self.logger.error(e)
            exit(3)


    def _get_db_connection(self):
        cnx = mysql.connector.connect(
            database=self._dict.DATABASE['NAME'],
            user=self._dict.DATABASE['USER'],
            password=self._dict.DATABASE['PASSWORD'],
            host=self._dict.DATABASE['HOST']
        )
        return cnx

    def get(self):
        return self._dict

    def get_logger(self):
        return self.logger
