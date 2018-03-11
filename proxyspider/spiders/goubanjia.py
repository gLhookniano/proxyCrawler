#!python3
#coding: utf-8
import re
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

class GoubanjiaSpider(scrapy.Spider):
    name = "GBJ"
    allowed_domains = ["goubanjia.com"]
    start_urls = [
    'http://www.goubanjia.com/free/gwgn/',
    'http://www.goubanjia.com/free/gngn/',
    ]

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
