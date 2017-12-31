# -*- coding: utf-8 -*-
import scrapy

class ZufangScrapyItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    # 区（朝阳）
    area = scrapy.Field()
    # 区域 (劲松)
    location = scrapy.Field()
    #小区 （劲松五区）
    housing_estate = scrapy.Field()
    # 租金
    rent = scrapy.Field()
    # 交租方式
    rent_type= scrapy.Field()
    # 建筑面积
    floor_area = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 朝向
    orientations = scrapy.Field()
    # 装修
    decoration = scrapy.Field()
    # 房源描述
    house_info = scrapy.Field()
    # 标签
    house_tags = scrapy.Field()


