import pytest

from mysql_clients.mysql_client import MysqlConnection
from tests.builder import MysqlBuilder


class TestMysql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder = MysqlBuilder(self.mysql)

    def test_coach_added(self):
        count = 0
        self.builder.add_coach('Ronald', 'Koeman', 'Barcelona')
        res = self.mysql.execute_query('SELECT * FROM coaches')
        # print('\n ' + str(res))
        for each in res:
            if each.get('name') == 'Ronald' and each.get('team') == 'Barcelona':
                count = count + 1
        assert count == 1
