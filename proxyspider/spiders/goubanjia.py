#!python3
#coding: utf-8
import re
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

class gbjSpider(scrapy.Spider):
    name = "gbj"

    def __init__(self, settings):
        super(gbjSpider, self).__init__()
        self.allowed_domains = settings["allowed_domains"]
        self.start_urls = settings['start_urls']
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings['GBJ_PATTERN']
        )
    def parse(self, response):
        for row in etree.HTML(response.body).xpath('//table//tr'):
            column = row.xpath('td')
            if column == []:
                continue
            
            ipport_str = ''
            for part in column[0]:
                ipport_style = part.xpath("@style")
                if ipport_style == "display: inline-block;" or ipport_sytle == []:
                    ipport_str += part.xpath("text()")
            parts = re.match(r'([.\d])+:(\d+)')
            
            item = proxyItem()
            item['address'] = parts.group(1)
            item['port'] = parts.group(2)
            item['protocol'] = ''.join(column[2].xpath('text()')).strip()
            yield item
