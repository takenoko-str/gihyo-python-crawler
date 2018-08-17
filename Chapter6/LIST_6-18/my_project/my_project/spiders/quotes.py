"""http://quotes.toscrape.com/ クローラー.

トップページのみをクロールして、Quoteを収集する.
"""
import scrapy
from scrapy.spiders import CrawlSpider

from my_project.items import Quote


class QuotesSpider(CrawlSpider):
    """Quoteアイテムを収集する."""

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        """クロールしたページからItemをスクレイピングする."""
        for i, quote_html in enumerate(response.css('div.quote')):
            # 試しに3件のアイテムを収集したら打ち切るようにしてみます
            if i > 2:
                raise scrapy.exceptions.CloseSpider(reason='abort')
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            yield item
