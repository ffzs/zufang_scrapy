# -*- coding: utf-8 -*-
import redis
from scrapy_redis.spiders import RedisSpider
from ..settings import *

class ZufangSpider(RedisSpider):  #这里是RedisSpider
    name = "zufang_up"
    allowed_domains = ["m.fang.com"]
    base_url = 'https://m.fang.com/zf/?purpose=%D7%A1%D5%AC&jhtype=zf&city=%B1%B1%BE%A9&renttype=cz&c=zf&a=ajaxGetList&city=bj&r=0.743897934517868&page='
    rds = redis.from_url(REDIS_URL,db=0,decode_responses=True)
    # for i in range(1, 3849):
    #     start_url = base_url+str(i)
    #     rds.rpush("zufang:start_urls", start_url)
    redis_key = "zufang:start_urls"

    def parse(self, response):
        urls = response.xpath('//a[@class="tongjihref"]/@href').extract()
        for url in urls:
            url = "https:"+url
            self.rds.rpush('zufang:house_urls', url)


