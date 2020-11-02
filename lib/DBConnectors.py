import logging
import requests
from requests.auth import HTTPBasicAuth
from mongoengine import connect
from functools import wraps
"""
Database connection decorators library
"""

class DBConnectors:
    def __init__(self, param):
        self.param = param

    def __call__(self, f):
        def f_decorated(instance):
            logging.info("decorated with param = %d" %
                         getattr(instance, self.param))
            return f(instance)
        return f_decorated

    @staticmethod
    def create_db_connection(f):
        """
        Creates a connection with specified db_name pre-configured or configured in case
        the kwargs contain mapping of DB name with host and Auth info
        :return:
        """
        @wraps(f)
        def wrapper(cls, *args, **kwargs):
            try:
                if not kwargs:
                    cls.mongo_client = connect(args.connection_name)
                else:
                    cls.mongo_client = connect.__call__(**kwargs)
            except ConnectionError as connException:
                logging.exception(connException)

        return wrapper

