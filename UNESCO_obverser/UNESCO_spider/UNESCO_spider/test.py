import MySQLdb

db_conn = MySQLdb.connect(db="UNESCO",
                            host="112.124.21.44",
                            user="root",
                            password="17872321501qQ#",
                            charset="utf8")
db_cursor = db_conn.cursor()
values = ('a',
          'a',
          '/en/news/2074',)
sql2 = 'update UNESCOnews set Detail = %s, dsrc= %s where Detail = %s'
db_cursor.execute(sql2, values)
db_conn.commit()
db_cursor.close()
db_conn.close()

