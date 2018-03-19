#!python3
#coding: utf-8
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem

class fplSpider(scrapy.Spider):
    name = "fpl"

    def __init__(self, settings):
        super(fplSpider, self).__init__()
        self.allowed_domains = settings["allowed_domains"]
        self.start_urls = settings['start_urls']
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings['FPL_PATTERN']
        )
    def parse(self, response):
        for row in etree.HTML(response.body).xpath("//table[@class='DataGrid']//tr")[1:]:
            sec_page = start_urls[0] + ''.join(row.xpath("td/a/@href"))
            yield scrapy.request(sec_page, callback=self.sec_parse)
            
    def sec_parse(self, response):
        for row in response.xpath("//table//tr[@class!='Caption']")[1:]:
            
            column = row.xpath("td")
            de_str = re.sub(r'IPDecode[(]"(.*?)"[)]', lambda _: _.group(1), ''.join(column[0].xpath(".//text()")))
            de_str = re.sub(r'%([0-9a-fA-F]+)', lambda _:unichr(int(_.group(1), 16)), de_str)
            de_str = re.sub(r'<.*?>', '', de_str).strip()
            
            item = proxyItem()
            item['address'] = de_str
            item['port'] = ''.join(column[1].xpath('text()')).strip()
            item['protocol'] = ''.join(column[2].xpath('text()')).strip()
            yield item
