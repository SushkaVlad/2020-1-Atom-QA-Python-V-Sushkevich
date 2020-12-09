from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Footballer(Base):
    __tablename__ = 'footballers'
    __table_args__ = {'mysql_charset': 'utf8'}

    tshirt_number = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(20), nullable=False)
    position = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Footballer(" \
               f"id='{self.tshirt_number}'," \
               f"name='{self.name}', " \
               f"surname='{self.surname}', " \
               f"start_teaching='{self.position}'" \
               f")>"


class Prepod(Base):
    __tablename__ = 'prepods'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(50), nullable=False)
    start_teaching = Column(Date, nullable=False, default='2020-01-01')


class CountsOfReq(Base):
    __tablename__ = 'NumberOfRequestsByType'
    __table_args = {'mysql_charset': 'utf8'}

    name_of_request = Column(String(20), primary_key=True, nullable=False)
    count_req = Column(Integer, nullable=False)


class TopTenSizes(Base):
    __tablename__ = 'TopTenSizes'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)
    req = Column(String(600), nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)


class TopTenSizesWithServerError(Base):
    __tablename__ = 'TopSizesWithServError'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)
    req = Column(String(600), nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)


class TopFreqUserError(Base):
    __tablename__ = 'TopFreqUserError'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    freq = Column(Integer, nullable=False)
    req = Column(String(600), nullable=False)
    code = Column(Integer, nullable=False)
