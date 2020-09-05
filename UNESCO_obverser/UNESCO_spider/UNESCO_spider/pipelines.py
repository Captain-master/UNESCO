# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import MySQLdb
from .items import UnescoSpiderItem, UnescocountryspiderItem, UnescokindspiderItem

class SpiderPipeline:
    #Spider开启，获取数据库配置信息，链接Mysql数据库服务器
    def open_spider(self, spider):
        pass
        # db_name = spider.settings.get("MYSQL_DB_NAME", "UNESCO")
        # host = spider.settings.get("MYSQL_HOST","112.124.21.44")
        # user = spider.settings.get("MYSQL_USER", "root")
        # pwd = spider.settings.get("MYSQL_PASSWORD", "17872321501qQ#")
        # self.db_conn = MySQLdb.connect(db=db_name,
        #                                host=host,
        #                                user=user,
        #                                password=pwd,
        #                                charset="utf8")
        # self.db_cursor = self.db_conn.cursor()

    def close_spider(self, spider):
        pass
        # self.db_conn.commit()
        # self.db_cursor.close()
        # self.db_conn.close()

#详情处理
class UnescodetailSpiderPipeline(SpiderPipeline):
    def process_item(self, item, spider):
        db_name = spider.settings.get("MYSQL_DB_NAME", "UNESCO")
        host = spider.settings.get("MYSQL_HOST", "112.124.21.44")
        user = spider.settings.get("MYSQL_USER", "root")
        pwd = spider.settings.get("MYSQL_PASSWORD", "17872321501qQ#")
        self.db_conn = MySQLdb.connect(db=db_name,
                                       host=host,
                                       user=user,
                                       password=pwd,
                                       charset="utf8")
        self.db_cursor = self.db_conn.cursor()
        # if isinstance(item, UnescoSpiderItem):
        #sql语句
        sql1 = 'select country_number from countrylist where country_name = %s'
        V1 = (item["country_name"],)
        self.db_cursor.execute(sql1, V1)
        item["country_name"] = self.db_cursor.fetchone()[0]
        print(item["country_name"])
        values = (item["name"],
                  item["detail"],
                  item["img_src"],
                  item["country_name"],
                  item["time"],)
        sql2 = 'insert into UNESCOlist(UNESCOname, detail, img_src,country_number, utime) values(%s,%s,%s,%s,%s)'
        self.db_cursor.execute(sql2, values)

        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()

        return item

class Unescocountryspiderpipline(SpiderPipeline):
    def process_item(self, item, spider):
        print('123')
        if isinstance(item,UnescocountryspiderItem):
            values = (item['country_name'],)
            sql = 'insert into countrylist(country_name) values(%s)'
            self.db_cursor.execute(sql, values)
            return item

class Unescokindspiderepipline(SpiderPipeline):
    def process_item(self, item, spider):
        db_name = spider.settings.get("MYSQL_DB_NAME", "UNESCO")
        host = spider.settings.get("MYSQL_HOST", "112.124.21.44")
        user = spider.settings.get("MYSQL_USER", "root")
        pwd = spider.settings.get("MYSQL_PASSWORD", "17872321501qQ#")
        self.db_conn = MySQLdb.connect(db=db_name,
                                       host=host,
                                       user=user,
                                       password=pwd,
                                       charset="utf8")
        self.db_cursor = self.db_conn.cursor()

        #if isinstance(item,UnescokindspiderItem):
        # sql = 'select UNESCOnumber from UNESCOlist where UNESCOname = %s'
        # self.db_cursor.execute(sql, values)
        # number = self.db_cursor.fetchone()
        # if number is not None:
        values = (item["kind"], item["name"],)
        sql2 = 'insert into UNESCOkind(UNESCOkind, UNESCOname) values(%s, %s)'
        self.db_cursor.execute(sql2, values)

        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()

class Unesconewspipline(SpiderPipeline):
    def process_item(self, item, spider):
        db_name = spider.settings.get("MYSQL_DB_NAME", "UNESCO")
        host = spider.settings.get("MYSQL_HOST", "112.124.21.44")
        user = spider.settings.get("MYSQL_USER", "root")
        pwd = spider.settings.get("MYSQL_PASSWORD", "17872321501qQ#")
        self.db_conn = MySQLdb.connect(db=db_name,
                                       host=host,
                                       user=user,
                                       password=pwd,
                                       charset="utf8")
        self.db_cursor = self.db_conn.cursor()
        values = (item["name"], item["time"], item["img_src"], item["sdetail"], item["Detail"], item["dsrc"], item["year"],)
        sql2 = 'insert into UNESCOnews(name,time,img_src,sdetail,Detail,dsrc,year) values(%s, %s, %s, %s, %s,%s,%s)'
        self.db_cursor.execute(sql2, values)

        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()
