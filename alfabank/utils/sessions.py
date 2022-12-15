import os
from alfabank.utils.requests_helper import BaseSession


def alfabank() -> BaseSession:
    api_url = os.getenv('API_URL')
    return BaseSession(base_url=api_url)