#!python3
#coding:utf-8
from scrapy.crawler import CrawlerProcess

from exspider.spiders.goubanjia import GoubanjiaSpider
from exspider.spiders.mimvp import MimvpSpider
from exspider.spiders.xici import XiciSpider
from exspider.spiders.freeproxylists import FPLSpider
from exspider.spiders.hidemyass import hidemyassSpider

if __name__ == '__main__':
    runner = CrawlerProcess()
#    runner.crawl(GoubanjiaSpider)
#    runner.crawl(MimvpSpider)
    runner.crawl(XiciSpider)
    runner.crawl(FPLSpider)
    runner.crawl(hidemyassSpider)
    runner.start()