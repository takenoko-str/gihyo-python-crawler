"""http://quotes.toscrape.com/ クローラー.

リンクを1階層だけクロールして、各ページにつき１個のQuoteを収集する.
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_project.items import Quote


class QuotesSpider(CrawlSpider):
    """Quoteアイテムを収集する."""

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(
            LinkExtractor(allow=r'.*'),
            callback='parse_start_url',
            follow=True,
        ),
    )

    def parse_start_url(self, response):
        """start_urlsのインデックスページもスクレイピングする."""
        return self.parse_item(response)

    def parse_item(self, response):
        """クロールしたページからItemをスクレイピングする."""
        # 1ページにつき1件のアイテムのみを収集してみます
        items = []
        for i, quote_html in enumerate(response.css('div.quote')):
            if i > 1:
                return items
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            items.append(item)
