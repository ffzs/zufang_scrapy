# -*- coding: utf-8 -*-

from zufang_scrapy.items import ZufangScrapyItem
from scrapy_redis.spiders import RedisSpider

class ZufangSpider(RedisSpider):
    name = "zufang_down"
    allowed_domains = ["m.fang.com"]
    redis_key = "zufang:house_urls"

    def parse(self, response):
        item = ZufangScrapyItem()
        item["title"] = response.xpath('//*[@class="xqCaption mb8"]/h1/text()')[0].extract()
        item["area"] = response.xpath('//*[@class="xqCaption mb8"]/p/a[2]/text()')[0].extract()
        item["location"] = response.xpath('//*[@class="xqCaption mb8"]/p/a[3]/text()')[0].extract()
        item["housing_estate"] = response.xpath('//*[@class="xqCaption mb8"]/p/a[1]/text()')[0].extract()
        item["rent"] = response.xpath('//*[@class="f18 red-df"]/text()')[0].extract()
        item["rent_type"] = response.xpath('//*[@class="f12 gray-8"]/text()')[0].extract()[1:-1]
        item["floor_area"] = response.xpath('//*[@class="flextable"]/li[3]/p/text()')[0].extract()[:-2]
        item["house_type"] = response.xpath('//*[@class="flextable"]/li[2]/p/text()')[0].extract()
        item["floor"] = response.xpath('//*[@class="flextable"]/li[4]/p/text()')[0].extract()
        item["orientations"] = response.xpath('//*[@class="flextable"]/li[5]/p/text()')[0].extract()
        item["decoration"] = response.xpath('//*[@class="flextable"]/li[6]/p/text()')[0].extract()
        item["house_info"] = response.xpath('//*[@class="xqIntro"]/p/text()')[0].extract()
        item["house_tags"] = ",".join(response.xpath('//*[@class="stag"]/span/text()').extract())

        yield item







