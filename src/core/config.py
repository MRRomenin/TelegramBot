import os
from logging import exception
from urllib.parse import urlparse  # parser env
from src.error.error import ErrorLing


class Parser:
    def __init__(self, config):
        self.config = config

    def parser_url(self) -> dict:
        pg_link = os.getenv(self.config)
        parsed_url = urlparse(pg_link)
        try:        # redo the errors
            if not parsed_url.scheme or not parsed_url.hostname:
                raise ValueError(f"not {parsed_url} link")
            db_config = {
                'dbname': parsed_url.path[1:],  # delete first '/'
                'user': parsed_url.username,
                'password': parsed_url.password,
                'host': parsed_url.hostname,
                'port': parsed_url.port or 5432,
            }
        except exception as e:
            raise ErrorLing(f"error parsing {e}")

        return db_config
