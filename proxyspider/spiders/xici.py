#coding: utf-8
import logging
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

logger = logging.getLogger(__name__)

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
    'http://www.xicidaili.com/nn',
    'http://www.xicidaili.com/nt',
    'http://www.xicidaili.com/wn',
    'http://www.xicidaili.com/wt',
    ]

    def parse(self, response):
        logger.info("parsing %s", response.url)
        for row in etree.HTML(response.body).xpath("//table//tr[@class]"):
            item = proxyItem()
            column = row.xpath("td")
            item['address'] = ''.join(column[1].xpath("text()")).strip()
            item['port'] = ''.join(column[2].xpath("text()")).strip()
            item['protocol'] = ''.join(column[5].xpath("text()")).strip()
            yield item