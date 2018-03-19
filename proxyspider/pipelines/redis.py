#coding:utf-8
import logging
from redis import Redis

logger = logging.getLogger(__name__)

class writeToSet(object):
#mysql/mariedb数据库写入
    def __init__(self, host, port, passwd, database_name=0):
        try:
            self.r = Redis(host=host, port=port, password=passwd, db=database_name)
        except Exception as err:
            logger.msg(err)
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings['REDIS_DB']['host'],
            port=crawler.settings['REDIS_DB']['port'],
            passwd=crawler.settings['REDIS_DB']['passwd'],
            database_name=crawler.settings['REDIS_DB']['database_name'],
        )

    def process_item(self, item, spider):
        p = self.r.pipeline()
        p.sadd('host', item["address"])
        p.sadd('port', item['port'])
        p.sadd('protocol', item["protocol"])
        p.execute()
        return item
