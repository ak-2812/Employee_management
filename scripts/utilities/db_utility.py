import psycopg2
from configparser import ConfigParser
from scripts.logging.application_logging import logger as log

from scripts.config import app_configurations


class RDBMSUtility(object):
    def __init__(self):
        """
            Initializer
        """
        try:

            config_path = 'conf/application.conf'

            config = ConfigParser()
            config.read(config_path)

            self.db_init_flag = 0

            self.db = psycopg2.connect(database=app_configurations.DB_NAME,
                                       user=app_configurations.USER,
                                       password=app_configurations.DB_PASSWORD,
                                       host=app_configurations.HOST)
            # print("Connection established successfully")
            log.info("Connection established successfully")
        except Exception as e:
            log.error(str(e), exc_info=True)
            raise Exception("Exception while establishing connection to database")

    def db_connection_close(self):
        """
            This function is to close connection to  Database
            :param :
            :return:
        """
        self.db.close()
        log.info("Destructor called, Connection deleted.")

    def execute_query(self, qry, required):
        """
            This function is to execute a given query
            :param :
            :return:
        """
        cursor = None
        try:
            cursor = self.db.cursor()
            cursor.execute(qry)
            rows = None
            self.db.commit()
            if required:
                rows = cursor.fetchall()
                return rows
            else:
                cursor.close()
                print("Executing query was Successful")
        except Exception as e:
            self.db.rollback()
            log.exception("Error executing query - {}".format(str(e)))
            raise Exception("Error executing the query")
        finally:
            if cursor:
                cursor.close()