import MySQLdb
import config
from exts import app

class operationmysql(object):
    def __init__(self):
        app.config.from_object(config)
        db_name = app.config["MYSQL_DB_NAME"]
        host = app.config["MYSQL_HOST"]
        user = app.config["MYSQL_USER"]
        pwd = app.config["MYSQL_PASSWORD"]
        self.db_conn = MySQLdb.connect(db=db_name,
                                       host=host,
                                       user=user,
                                       password=pwd,
                                       charset="utf8")
        self.db_cursor = self.db_conn.cursor(MySQLdb.cursors.DictCursor)

    def search(self, sql, values=None):
        try:
            self.db_cursor.execute(sql, values)
            data = self.db_cursor.fetchall()
            return data
        except MySQLdb.Error:
            print("Mysqldb Error:")
        finally:
            self.db_conn.commit()
            self.db_cursor.close()
            self.db_conn.close()

    def operation(self,sql):
        try:
            self.db_cursor.execute(sql)
        except MySQLdb.Error:
            print("Mysqldb Error:")
        finally:
            self.db_conn.commit()
            self.db_cursor.close()
            self.db_conn.close()
