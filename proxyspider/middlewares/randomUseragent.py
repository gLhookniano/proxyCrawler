#coding:utf-8
import random
import logging
from lxml import etree

logger = logging.getLogger(__name__)

class randomUseragent(object):
    def __init__(self, settings):
        loc_proxy_list = settings.get('LOC_USERAGENT_LIST')
        useragent_platform = settings.get('USERAGENT_PLATFORM')
  
        if loc_proxy_list:
            with open(loc_proxy_list, 'r') as fp:
                selector = etree.HTML(fp.read())
                if not useragent_platform:
                    
                    ua_xpath = r'//@useragent'
                else:
                    #selector 
                    ua_xpath = r"//folder[@description='{}']".format(useragent_platform) +r"//@useragent"
           
                self.useragent = selector.xpath(ua_xpath)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
                
    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.useragent)

    def process_exception(self, request, exception, spider):
        logger.debug('Request url: %s with User-Agent: <%s> fail.' % (
                    request.url, request.headers["User-Agent"]))
