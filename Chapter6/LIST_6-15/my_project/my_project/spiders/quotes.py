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
        items = []
        for quote_html in response.css('div.quote'):
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            items.append(item)
        return items
