#coding:utf-8
import logging
import mysql

logger = logging.getLogger(__name__)

class writeTo(object):
'''
mysql/mariedb数据库写入
'''
    def __init__(self, host, port, username, passwd, database_name, table_name):
        config_args = {
            'user':username,
            'password':passwd,
            'host':host,
            'database':database_name,
            'charset':'utf-8',
            'use_unicode':True,
            'raise_on_warnings':True
        }
        
        try:
            self.cnx = mysql.connector.connect(**config_args)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_DB', 'host'),
            port=crawler.settings.get('MYSQL_DB', 'port'),
            username=crawler.settings.get('MYSQL_DB', 'username'),
            passwd=crawler.settings.get('MYSQL_DB', 'passwd'),
            database_name=crawler.settings.get('MYSQL_DB', 'database_name'),
            table_name=crawler.settings.get('MYSQL_DB', 'table_name'),
        )
        
    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        sql ="insert into devdb.tb_ip (hash256, protocol, address, port, position, anonymity, speed, live) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        sql_value = (
            item["hash256"], 
            item["protocol"],
            item["address"],
            item["port"],
            item["position"],
            item["anonymity"],
            item["speed"],
            item["live"],
            item["check_time"]
            )
        
        self.cursor.execute(sql, sql_value)
        self.cnx.commit()
        return item
