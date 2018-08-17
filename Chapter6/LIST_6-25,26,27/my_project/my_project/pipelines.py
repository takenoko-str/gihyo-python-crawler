"""Quotesアイテムを処理するパイプライン."""
from hashlib import sha256

from orator import DatabaseManager, Model
from orator.orm import belongs_to_many

from my_project.settings import ORATOR_CONFIG


db = DatabaseManager(ORATOR_CONFIG)
Model.set_connection_resolver(db)


class Quote(Model):
    """quotesテーブルモデル."""

    @belongs_to_many
    def tags(self):
        return Tag


class Tag(Model):
    """tagsテーブルモデル."""

    @belongs_to_many
    def quote(self):
        return Quote


class DatabasePipeline(object):
    """MySQLにQuotesを保存する."""

    def __init__(self):
        """スクレイピングした全itemを格納する変数を用意する."""
        self.items = []

    def process_item(self, item, spider):
        """各アイテムに対する処理."""
        self.items.append(item)
        return item

    def close_spider(self, spider):
        """spider終了時の処理."""
        for item in self.items:
            text_hash = sha256(
                item['text'].encode('utf8', 'ignore')).hexdigest()
            exist_quote = Quote.where('text_hash', text_hash).get()
            if exist_quote:
                continue
            quote = Quote()
            quote.author = item['author']
            quote.text = item['text']
            quote.text_hash = text_hash
            quote.save()

            tags = []
            for tag_name in item['tags']:
                tag = Tag.where('name', tag_name).first()
                if not tag:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                tags.append(tag)
                quote_tags = quote.tags()
                quote_tags.save(tag)
