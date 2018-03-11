#coding:utf-8
import logging
import json
import random

logger = logging.getLogger(__name__)

class randomProxy(object):
'''
proxy csv format : {"address": "171.212.200.116", "port": "7777", "protocol": "HTTP"}
request proxy format : http://username:password@some_proxy_server:port
'''
    def __init__(self, settings):
        loc_proxy_list = settings.get('LOC_PROXY_LIST')
        self.proxy_list = []
        if loc_proxy_list:
            with open(loc_proxy_list, 'r') as fp:
                for line in fp.readlines():
                    j=json.loads(line)
                    self.proxy_list.append(r'http://' + j["address"] + ':' + j["port"])

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    
    def process_request(self, request, spider):
        meta_proxy = random.choice(self.proxy_list)
        request.meta['proxy'] = meta_proxy

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        logger.msg('Removing failed proxy <%s>, %d proxies left' % (
                    proxy, len(self.proxy_list)))
        try:
            del self.proxy_list[proxy]
        except ValueError:
            pass
