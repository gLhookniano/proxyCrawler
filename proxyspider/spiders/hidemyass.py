#!python3
#coding: utf-8
import re
import scrapy
from lxml import etree
from proxyspider.items.proxy import proxyItem


class hidemyassSpider(scrapy.Spider):
    name = "HMA"
    allowed_domains = ["proxylist.hidemyass.com"]
    start_urls = ['http://proxylist.hidemyass.com/']

    def parse(self, response):
        for row in etree.HTML(response.body).xpath("//table//tr")[1:]:
            column = row.xpath("td")
            
            mix_pats = ''.join(column[1].xpath("span/style/text()"))
            mix_text = re.sub(r'[\t\n\r\b]*', '', etree.tostring(column[1]).strip())
            mix_text = re.sub(r'<style>.*?</style>', '', mix_text)
            for pattens in re.findall(r'.(\w+){(display:[ ]?\w+)}', mix_pats):
                mix_text = re.sub(r'<\w+ ([\w]{4,5})=["](.*?)["]>(.*?)</\w+>', lambda _:self._decodeip(_, pattens), mix_text)
            mix_text = re.sub(r'<.*?>', '', mix_text).strip()

            item = proxyItem()
            item['protocol'] = ''.join(column[6].xpath("text()")).strip()
            item['address'] = mix_text
            item['port'] = ''.join(column[2].xpath('text()')).strip()
            yield item

    def _decodeip(self, matchoj, pattens):
        if matchoj.group(1) == 'style':
            if matchoj.group(2) == "display:none":
                return ''
            return matchoj.group(3)
        if matchoj.group(2) == pattens[0]:
            if pattens[1] == "display:none":
                return ''
            return matchoj.group(3)
        return matchoj.group(0)
