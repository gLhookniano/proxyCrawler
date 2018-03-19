# proxySpider
get proxy ip from proxy-website, use scrapy

## Requirements :
* scrapy lxml pymysql pymongo

## support databases :
* mysql
* mongo

## support website :
    66ip cnproxy cz88 freeproxylist hidemyass incloak ip181 kuaidaili mimiip mimvp xici

## middleware :
* random useragent
* random proxy

## How to use:
1. open `proxyspider/settings.py` modify option to fit your environment.
2. databases settings:
    1. mysql 
        1. modify `./DB/mysql_setup.sh`
        2. `sh ./DB/mysql_setup.sh`
    2. mongo
        1. modify `./DB/mongo_setup.sh`
        2. `sh ./DB/mongo_setup.sh`
    3. redis
        1. modify `./DB/mongo_setup.sh`
        2. `sh ./DB/mongo_setup.sh`
3. `python ./run.py`

