import os
from urllib.parse import urlparse #parser env

class Parser:
    def __init__(self, config):
        self.config = config

    def parser_url(self):
        pg_link = os.getenv(self.config)
        parsed_url = urlparse(pg_link)

        db_config = {
                'dbname': parsed_url.path[1:],  # delete first '/'
                'user': parsed_url.username,
                'password': parsed_url.password,
                'host': parsed_url.hostname,
                'port': parsed_url.port,
            }

        return db_config