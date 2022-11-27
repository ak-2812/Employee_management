import configparser

config = configparser.ConfigParser()
config.read('conf/application.conf')

db_conf = configparser.ConfigParser()
db_conf.read('conf/db.conf')

api_base_service_url = "/fastapi/template"

LOG_LEVEL = config.get('LOG', 'log_level')
LOG_BASEPATH = config.get('LOG', 'base_path')
LOG_FILE_NAME = LOG_BASEPATH + config.get('LOG', 'file_name')
LOG_HANDLERS = config.get('LOG', 'handlers')
LOGGER_NAME = config.get('LOG', 'logger_name')

"""
PostGreSQL config info
"""
HOST = config.get("POSTGRESQL", "host")
USER = config.get("POSTGRESQL", "user")
DB_NAME = config.get("POSTGRESQL", "database")
DB_PASSWORD = config.get("POSTGRESQL", "password", fallback='')