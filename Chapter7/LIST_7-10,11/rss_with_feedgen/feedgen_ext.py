"""feedgen拡張名前空間 (book: http://my-service.com/xmlns/book)."""
from lxml import etree

from feedgen.ext.base import BaseExtension


class BookBaseExtension(BaseExtension):
    """book拡張名前空間."""

    # 独自名前空間のURL
    BOOK_NS = "http://my-service.com/xmlns/book"

    def __init__(self):
        """独自に追加する要素名 writer に __ を付けてインスタンス変数を作成."""
        # 変数は辞書型で受け取る想定
        self.__writer = {}

    def extend_ns(self):
        """拡張名前空間."""
        return {'book': self.BOOK_NS}

    def _extend_xml(self, elm):
        """要素の追加."""
        if self.__writer:
            writer = etree.SubElement(
                elm,  # writer要素を従属させる親要素
                '{%s}writer' % self.BOOK_NS,  # {名前空間のURL}要素名
                attrib={'id': self.__writer.get('id')}  # id属性の適用
            )
            writer.text = self.__writer.get('name')  # 要素の内容の適用
        return elm

    def writer(self, name_and_id_dict=None):
        """self.__writerへの受け渡し."""
        if name_and_id_dict is not None:
            name = name_and_id_dict.get('name')
            id_ = name_and_id_dict.get('id')
            if name and id_:
                self.__writer = {'name': name, 'id': id_}
            elif not name and not id_:  # 要素の内容 name が無い場合は要素を作成しない
                self.__writer = {}
            else:
                raise ValueError('nameとidは両方セットしてください.')
        return self.__writer


class BookFeedExtension(BookBaseExtension):
    """channel要素に適用."""

    def extend_rss(self, rss_feed):
        """要素の追加時に呼ばれる."""
        channel = rss_feed[0]
        self._extend_xml(channel)


class BookEntryExtension(BookBaseExtension):
    """item要素に適用."""

    def extend_rss(self, entry):
        """要素の追加時に呼ばれる."""
        self._extend_xml(entry)
