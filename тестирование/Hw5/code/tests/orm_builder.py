from faker import Faker
from models.models import Base, Footballer, CountsOfReq, TopTenSizes, TopTenSizesWithServerError, \
    TopFreqUserError
from mysql_clients.mysql_orm_client import MysqlOrmConnection

fake = Faker(locale='ru_RU')


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

        self.drop_NumberOfRequestsByType()
        self.create_NumberOfRequestsByType()
        self.drop_TopTenSizes()
        self.create_TopTenSizes()
        self.drop_TopSizesWithServError()
        self.create_TopSizesWithServError()
        self.drop_TopFreqUserError()
        self.create_TopFreqUserError()
        self.drop_footballers()

    def create_footballers(self):
        if not self.engine.dialect.has_table(self.engine, 'footballers'):
            Base.metadata.tables['footballers'].create(self.engine)

    def drop_footballers(self):
        if self.engine.dialect.has_table(self.engine, 'footballers'):
            Base.metadata.tables['footballers'].drop(self.engine)

    def add_footballer(self, tshirt_number, name, last_name, position):
        footballer = Footballer(
            tshirt_number=tshirt_number,
            name=name,
            surname=last_name,
            position=position
        )
        self.connection.session.add(footballer)
        self.connection.session.commit()
        return footballer

    def create_NumberOfRequestsByType(self):
        if not self.engine.dialect.has_table(self.engine, 'NumberOfRequestsByType'):
            Base.metadata.tables['NumberOfRequestsByType'].create(self.engine)

    def drop_NumberOfRequestsByType(self):
        if self.engine.dialect.has_table(self.engine, 'NumberOfRequestsByType'):
            Base.metadata.tables['NumberOfRequestsByType'].drop(self.engine)

    def add_CountOfReq(self, name_of_req, number):
        count = CountsOfReq(
            name_of_request=name_of_req,
            count_req=number
        )

        self.connection.session.add(count)
        self.connection.session.commit()
        return count

    def create_TopTenSizes(self):
        if not self.engine.dialect.has_table(self.engine, 'TopTenSizes'):
            Base.metadata.tables['TopTenSizes'].create(self.engine)

    def drop_TopTenSizes(self):
        if self.engine.dialect.has_table(self.engine, 'TopTenSizes'):
            Base.metadata.tables['TopTenSizes'].drop(self.engine)

    def add_TopTenSizes(self, ip, req, code, size):
        top_sizes = TopTenSizes(
            ip=ip,
            req=req,
            code=code,
            size=size
        )

        self.connection.session.add(top_sizes)
        self.connection.session.commit()
        return top_sizes

    def create_TopSizesWithServError(self):
        if not self.engine.dialect.has_table(self.engine, 'TopSizesWithServError'):
            Base.metadata.tables['TopSizesWithServError'].create(self.engine)

    def drop_TopSizesWithServError(self):
        if self.engine.dialect.has_table(self.engine, 'TopSizesWithServError'):
            Base.metadata.tables['TopSizesWithServError'].drop(self.engine)

    def add_TopSizesWithServError(self, ip, req, code, size):
        top_sizes_with_serv_error = TopTenSizesWithServerError(
            ip=ip,
            req=req,
            code=code,
            size=size
        )

        self.connection.session.add(top_sizes_with_serv_error)
        self.connection.session.commit()
        return top_sizes_with_serv_error

    def create_TopFreqUserError(self):
        if not self.engine.dialect.has_table(self.engine, 'TopFreqUserError'):
            Base.metadata.tables['TopFreqUserError'].create(self.engine)

    def drop_TopFreqUserError(self):
        if self.engine.dialect.has_table(self.engine, 'TopFreqUserError'):
            Base.metadata.tables['TopFreqUserError'].drop(self.engine)

    def add_TopFreqUserError(self, freq, req, code):
        top_freq_user_error = TopFreqUserError(
            freq=freq,
            req=req,
            code=code
        )

        self.connection.session.add(top_freq_user_error)
        self.connection.session.commit()
        return top_freq_user_error
