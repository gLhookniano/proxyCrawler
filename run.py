#!python3
#coding:utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from proxyspider.spiders.goubanjia import GoubanjiaSpider
from proxyspider.spiders.mimvp import MimvpSpider
from proxyspider.spiders.xici import XiciSpider
from proxyspider.spiders.freeproxylists import FPLSpider
from proxyspider.spiders.hidemyass import hidemyassSpider

if __name__ == '__main__':
    runner = CrawlerProcess(get_project_settings())
#    runner.crawl(GoubanjiaSpider)
#    runner.crawl(MimvpSpider)
    runner.crawl(XiciSpider)
#    runner.crawl(FPLSpider)
#    runner.crawl(hidemyassSpider)
    runner.start()
    