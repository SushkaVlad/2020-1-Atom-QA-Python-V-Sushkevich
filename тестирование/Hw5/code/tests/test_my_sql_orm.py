import pytest
from models.models import Footballer
from mysql_clients.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test_if_table_created(self):
        self.builder.create_footballers()
        self.mysql.session.commit()
        assert self.mysql.connection.engine.dialect.has_table(self.mysql.connection.engine, 'footballers')

    def test_if_footballer_added(self):
        self.builder.create_footballers()
        self.mysql.session.commit()
        self.builder.add_footballer(10, 'Lionel', 'Messi', 'forward')
        player = self.mysql.session.query(Footballer).filter_by(tshirt_number=10).first()
        assert player.name == 'Lionel'
