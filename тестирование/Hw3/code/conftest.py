from dataclasses import dataclass
import pytest
from api_client.mytarget_client import MyTargetClient


@dataclass
class Settings:
    URL: str = None
    LOGIN: str = None
    PASSWORD: str = None


@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(URL='https://target.my.com/',
                        LOGIN='vladislav2908@gmail.com',
                        PASSWORD='technoatom2020')
    return settings


@pytest.fixture(scope='function')
def mytarget_api_client(config):
    return MyTargetClient(config.URL, config.LOGIN, config.PASSWORD)
