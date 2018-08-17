"""feedgenで青空文庫の芥川龍之介の新作フィードを出力する."""
from feedgen.feed import FeedGenerator

# feedgen_ext.py からchannel要素用とitem要素用の
# 独自名前空間拡張用クラスをインポート
from feedgen_ext import BookEntryExtension, BookFeedExtension


def create_feed():
    """RSSフィードの生成."""

    # フィードデータ格納用
    fg = FeedGenerator()

    # 独自名前空間の登録と、独自名前空間の拡張用クラスの適用
    fg.register_extension(
        'book',
        extension_class_feed=BookFeedExtension,
        extension_class_entry=BookEntryExtension,
    )

    # <channel><title>要素
    fg.title("芥川龍之介の新着作品")
    # <channel><link>要素: <link>タグの内容は href で指定
    fg.link(href="http://www.aozora.gr.jp/index_pages/person879.html")
    # <channel><description>要素
    fg.description("青空文庫に追加された芥川龍之介の新着作品のフィード")

    # <channel><item>要素の追加
    fe = fg.add_entry()
    # <channel><item><title>要素
    fe.title("羅生門")
    # <channel><item><link>要素
    fe.link(href="http://www.aozora.gr.jp/cards/000879/card128.html")
    # <channel><item><description>要素
    fe.description(
        '<a href="http://www.aozora.gr.jp/index_pages/person879.html">芥川</a>の5作目の短編小説。'
        "次の作品『今昔物語集』巻二十九「羅城門登上層見死人盗人語第十八」"
        "に題材を取り、人間のエゴイズムについて"
        "作者自身の解釈を加えたものである。")
    # <channel><item><book:writer>要素 (独自名前空間を持つ要素)
    fe.book.writer({'name': "芥川 竜之介", 'id': "879"})  # 値は辞書型変数で渡す

    # フィードデータをRSSフォーマットに変換する (pretty=True で整形)
    return fg.rss_str(pretty=True)


if __name__ == '__main__':
    rss_str = create_feed()
    print(rss_str.decode())
