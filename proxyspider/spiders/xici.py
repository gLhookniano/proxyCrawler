#coding: utf-8
import logging
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

logger = logging.getLogger(__name__)

class xiciSpider(scrapy.Spider):
    name = "xici"
    
    def __init__(self, settings):
        super(xiciSpider, self).__init__()
        self.allowed_domains = settings["allowed_domains"]
        self.start_urls = settings['start_urls']
        self.xpath = settings['xpath']
        self.item_xpath = settings['item_xpath']
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings['XICI_PATTERN']
        )
        
    def parse(self, response):
        logger.info("parsing %s", response.url)
        for row in etree.HTML(response.body).xpath(self.xpath):
            item = proxyItem()
            if not self.item_xpath['address']:
                item['address']=''
            else:
                item['address'] = row.xpath(self.item_xpath['address'])[0]
            if not self.item_xpath['port']:
                item['port']=''
            else:
                item['port'] = row.xpath(self.item_xpath['port'])[0]
            if not self.item_xpath['protocol']:
                item['protocol'] = ''
            else:
                item['protocol'] = row.xpath(self.item_xpath['protocol'])[0]
            yield item