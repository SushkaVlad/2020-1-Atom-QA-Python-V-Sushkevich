import pytest

from api_client.mytarget_client import MyTargetClient
from conftest import Settings


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.config: Settings = config
        self.target_client: MyTargetClient = request.getfixturevalue('mytarget_api_client')
