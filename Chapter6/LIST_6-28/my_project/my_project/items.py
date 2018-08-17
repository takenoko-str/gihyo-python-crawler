"""有名人の引用アイテム."""
import scrapy


class Quote(scrapy.Item):
    """有名人の引用アイテム."""
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
