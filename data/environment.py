import os


class Environment:
    SHOT = 'shot'
    PROD = 'prod'

    URLS = {
        SHOT: 'https://example.ru/',
        PROD: 'https://www.saucedemo.com/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Environment()