#!python3
#coding: utf-8
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

class MimvpSpider(scrapy.Spider):
    name = "mimvp"
    allowed_domains = ["proxy.mimvp.com"]
    start_urls = [
        'http://proxy.mimvp.com/free.php?proxy=in_hp',
        'http://proxy.mimvp.com/free.php?proxy=out_hp',
        'http://proxy.mimvp.com/free.php?proxy=in_socks',
        'http://proxy.mimvp.com/free.php?proxy=out_socks',
    ]

    def parse(self, response):
        for row in etree.HTML(response.body).xpath("//table//tr"):
            column = row.xpath("td")
            if column == []:
                continue
            
            item = proxyItem()
            item['protocol'] = ''.join(column[3].xpath("text()")).strip()
            item['address'] = ''.join(column[1].xpath("text()")).strip()
            item['port'] = ''.join(column[2].xpath('text()')).strip()
            yield item
            
    def _picture_parse(self, response):
        pass