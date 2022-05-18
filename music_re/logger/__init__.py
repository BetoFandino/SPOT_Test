import logging
import sys

from . import consts


_config_loaded = False


def load_config():
    global _config_loaded
    if _config_loaded:
        return

    import logging.config
    import os

    # Logging facility
    log_directory = os.environ.get('LOG_DIRECTORY', '')
    app_log_file_name = os.path.abspath(os.path.join(log_directory, 'app.log'))

    if not app_log_file_name:
        logging.error('LOG_DIRECTORY must be defined in the os environment')
        exit(-1)

    app_log_path = os.path.split(app_log_file_name)[0]
    # if not dir_is_writable(app_log_path):
    #     logging.error(f'LOG_DIRECTORY is not writable by the process: "{app_log_path}"')
    #     exit(-1)

    logging_level = os.environ.get('LOGGING_LEVEL', 'ERROR')
    key = 'LOGGING_LEVEL_message_done'
    if not os.environ.get(key):
        os.environ[key] = '1'
        is_running_manage = 'manage.py' in sys.argv[0]
        if not is_running_manage:
            logging.error(f'>>> Using LOGGING_LEVEL={logging_level}')

    # noinspection SpellCheckingInspection
    logger_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'handlers': {
            consts.CONSOLE_HANDLER: {
                'level': logging_level,
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            consts.APP_LOG_FILE_HANDLER: {
                'level': logging_level,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': app_log_file_name,
                'maxBytes': 1024 * 1024 * 5,  # 5MB
                'backupCount': 0,
                'formatter': 'simple',
                'encoding': 'UTF-8'
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s|%(asctime)s|%(funcName)s --> %(message)s',
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s|%(asctime)s --> %(message)s',
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
        'loggers': {
            consts.APP_LOGGER: {
                'handlers': [consts.CONSOLE_HANDLER, consts.APP_LOG_FILE_HANDLER],
                'level': logging_level,
                'propagate': False,
            },
        }
    }

    logging.config.dictConfig(logger_config)
    _config_loaded = True


def get_logger():
    if not _config_loaded:
        load_config()

    return logging.getLogger(consts.APP_LOGGER)
