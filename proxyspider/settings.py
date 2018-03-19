# -*- coding: utf-8 -*-

# Scrapy settings for proxyspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'proxyspider'

SPIDER_MODULES = ['proxyspider.spiders']
NEWSPIDER_MODULE = 'proxyspider.spiders'

LOG_FILE=r"./log.log"
LOG_ENCODING="utf-8"
LOG_ENABLED=True

#**********************CUSTOM SETTINGS START******************************
LOC_PROXY_LIST=r"./proxyspider/util/proxylist.csv"
LOC_USERAGENT_LIST=r"./proxyspider/util/useragentswitcher.xml"
USERAGENT_FILTER=r'Windows'#Windows Mac Linux Unix Mobile Spiders Miscellaneous

LOC_WRITE_JSON=r"./x.json"
LOC_WRITE_CSV=r"./x.csv"

MYSQL_DB={
    "host":"192.168.63.131",
    "port":"3306",
    "username":"dev",
    "passwd":"dev",
    "database_name":"devdb",
    "table_name":"tb_ip",
}

MONGO_DB={
    "host":"192.168.63.133",
    "port":"27017",
    "username":"dev",
    "passwd":"dev",
    "database_name":"devdb",
    "collection_name":"test",
}

REDIS_DB={
    "host":"192.168.63.134",
    "port":"6379",
    "passwd":"dev",
    "database_name":"0",
}

#usual_xpath
XICI_PATTERN=dict(
    allowed_domains=["xicidaili.com"],
    start_urls=["http://www.xicidaili.com/{}/{}".format(i,j) for i in ['nn','nt','wn','wt'] for j in range(1,10)],
    xpath=r"//table/tr[position()>1]",
    item_xpath={
        'address':r'td[2]/text()',
        'port':r'td[3]/text()',
        'protocol':r'td[6]/text()',
        }
    )
_66IP_PATTERN=dict(
    allowed_domains=["66ip.cn"],
    start_urls=['http://www.66ip.cn/%s.html' % n for n in ['index'] + list(range(2, 34))] + ['http://www.66ip.cn/areaindex_%s/%s.html' % (m, n) for m in range(1, 34) for n in range(1, 10)],
    xpath="//table/tr[position()>1]",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':None,
        }
    )
CNPROXY_PATTERN=dict(
    allowed_domains=["cn-proxy.com"],
    start_urls=['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218'],
    xpath="//table[@class='sortable']/tbody/tr",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':None,
        }
    )
MIMIIP_PATTERN=dict(
    allowed_domains=["mimiip.com"],
    start_urls=['http://www.mimiip.com/gngao/%s' % n for n in range(1, 10)],
    xpath="//table[@class='list']/tr[position()>1]",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':None,
        }
    )
INCLOAK_PATTERN=dict(
    allowed_domains=["incloak.com"],
    start_urls=['http://incloak.com/proxy-list/%s#list' % n for n in ([''] + ['?start=%s' % (64 * m) for m in range(1, 10)])],
    xpath="//table[@class='proxy__t']/tbody/tr",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':None,
        }
    )
KUAIDAILI_PATTERN=dict(
    allowed_domains=["kuaidaili.com"],
    start_urls=['http://www.kuaidaili.com/proxylist/%s/' % n for n in range(1, 11)] + ['http://www.kuaidaili.com/free/%s/%s/' %(m, n) for m in ['inha','intr','outha','outtr'] for n in range(1,11)],
    xpath="//*[@id='freelist' or 'list']/table/tbody/tr",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':'td[4]/text()',
        }
    )
CZ88_PATTERN=dict(
    allowed_domains=["cz88.net"],
    start_urls=['http://www.cz88.net/proxy/%s' % m for m in ['index.shtml'] + ['http_%s.shtml' % n for n in range(2, 11)]],
    xpath="//*[@id='boxright']/div/ul/li[position()>1]",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':'td[3]/text()',
        }
    )
IP181_PATTERN=dict(
    allowed_domains=["ip181.com"],
    start_urls=['http://www.ip181.com/daili/%s.html' % n for n in range(1, 11)],
    xpath="//div[@class='row']/div[3]/table/tbody/tr[position()>1]",
    item_xpath={
        'address':'td[1]/text()',
        'port':'td[2]/text()',
        'protocol':'td[4]/text()',
        }
    )

    
#special
GBJ_PATTERN=dict(
    allowed_domains=["goubanjia.com"],
    start_urls=["http://www.goubanjia.com"],
    )
HMA_PATTERN=dict(
    allowed_domains=["proxylist.hidemyass.com"],
    start_urls=['http://proxylist.hidemyass.com/'],
    )
FPL_PATTERN=dict(
    allowed_domains = ["freeproxylists.net"],
    start_urls = ['http://freeproxylists.net/country/'],
    )
MIMVP_PATTERN=dict(
    allowed_domains = ["proxy.mimvp.com"],
    start_urls = ['https://proxy.mimvp.com/free.php?proxy={}&sort=&page={}'.format(i,j) for i in ['in_hp','out_hp','in_socks','out_socks'] for j in range(1,10)],
    xpath="//div[@class='free-list']/table/tbody/tr",
    item_xpath={
        'address':'td[2]/text()',
        'port':None,
        'protocol':'td[4]/text()',
        }
    )
#***********************CUSTOM SETTINGS END*********************************

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxyspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   	'User-Agent' : 'Mozilla/5.0 (Windows; Windows NT 5.1; en-US; rv:1.7.8) Gecko/20050511 Firefox/1.0.4',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'proxyspider.middlewares.ProxyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'proxyspider.middlewares.randomUseragent.randomUseragent': 543,
#    'proxyspider.middlewares.randomProxy.randomProxy': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'proxyspider.pipelines.json.dumpTo': 300,
#    'proxyspider.pipelines.mysql.writeTo': 301,
#    'proxyspider.pipelines.csv.writeTo': 302,
#    'proxyspider.pipelines.csv.hashWriteTo': 303,
#    'proxyspider.pipelines.mongo.writeTo': 304,
#    'proxyspider.pipelines.redis.writeToSet': 305,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
