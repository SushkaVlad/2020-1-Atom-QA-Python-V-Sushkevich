import pytest

from mysql_clients.mysql_client import MysqlConnection
from mysql_clients.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection(user='root', password='123', db_name='TEST_PYTHON')


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user='root', password='123', db_name='TEST_PYTHON_ORM')
