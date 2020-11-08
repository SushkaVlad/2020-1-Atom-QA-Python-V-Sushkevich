from mysql_clients.mysql_client import MysqlConnection

class MysqlBuilder(object):
    def __init__(self, connection: MysqlConnection):
        self.connection = connection

        self.create_coaches()


    def create_coaches(self):
        coaches_query = """
           CREATE TABLE IF NOT EXISTS `coaches` (
             `id` smallint(6) NOT NULL AUTO_INCREMENT,
             `name` char(20) NOT NULL,
             `surname` char(50) NOT NULL,
             `team` char(20) NOT NULL,
             PRIMARY KEY (`id`)
           ) CHARSET=utf8
           """
        self.connection.execute_query(coaches_query)


    def add_coach(self, name, surname, team):
        insert_query = f"INSERT INTO coaches(name, surname, team)" \
                       f"VALUES('{name}', '{surname}', '{team}')"
        self.connection.execute_query(insert_query)
