#!python3
#coding:utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from proxyspider.spiders._66ip import _66ipSpider
from proxyspider.spiders.cnproxy import cnproxySpider
from proxyspider.spiders.cz88 import cz88Spider
from proxyspider.spiders.freeproxylists import fplSpider
from proxyspider.spiders.goubanjia import gbjSpider
from proxyspider.spiders.hidemyass import hmaSpider
from proxyspider.spiders.incloak import incloakSpider
from proxyspider.spiders.ip181 import ip181Spider
from proxyspider.spiders.kuaidaili import kuaidailiSpider
from proxyspider.spiders.mimiip import mimiipSpider
from proxyspider.spiders.mimvp import mimvpSpider
from proxyspider.spiders.xici import xiciSpider


if __name__ == '__main__':
    runner = CrawlerProcess(get_project_settings())
#    runner.crawl(_66ipSpider)
#    runner.crawl(cnproxySpider)
#    runner.crawl(cz88Spider)
#    runner.crawl(fplSpider)
#    runner.crawl(gbjSpider)
#    runner.crawl(hmaSpider)
    runner.crawl(incloakSpider)
    runner.crawl(ip181Spider)
    runner.crawl(kuaidailiSpider)
    runner.crawl(mimiipSpider)
    runner.crawl(mimvpSpider)
    runner.crawl(xiciSpider)
    runner.start()
    