"""xml.etree.ElementTree でRSSを作る."""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 独自名前空間の定義 (http://my-service.com/xmlns/book は例です)
NAMESPACES = {'book': 'http://my-service.com/xmlns/book'}


def create_rss():
    """RSSを作る."""
    for ns_name, ns_uri in NAMESPACES.items():
        ET.register_namespace(ns_name, ns_uri)  # 名前空間の登録

    # <rss>要素の作成
    elm_rss = ET.Element(
        "rss",
        attrib={
            'version': "2.0",
            'xmlns:book': NAMESPACES['book']
        },
    )

    # <channel>要素の作成
    elm_channel = ET.SubElement(elm_rss, 'channel')

    # channel要素のサブ要素を一括で追加する
    channel_sources = {
        'title': "芥川龍之介の新着作品",
        'link': "http://www.aozora.gr.jp/index_pages/person879.html",
        'description': "青空文庫に追加された芥川龍之介の新着作品のフィード",
    }
    children_of_channel = []
    for tag, text in channel_sources.items():
        child_elm_of_channel = ET.Element(tag)
        child_elm_of_channel.text = text
        children_of_channel.append(child_elm_of_channel)

    # 一括で要素を追加
    elm_channel.extend(children_of_channel)

    # <item>要素の追加: 一つずつサブ要素を追加している
    elm_item = ET.SubElement(elm_channel, 'item')

    # <item><title>要素の追加
    elm_item_title = ET.SubElement(elm_item, 'title')
    elm_item_title.text = "羅生門"

    # <item><link>要素の追加
    elm_item_link = ET.SubElement(elm_item, 'link')
    elm_item_link.text \
        = "http://www.aozora.gr.jp/cards/000879/card128.html"

    # <item><description>要素の追加
    elm_item_description = ET.SubElement(elm_item, 'description')
    elm_item_description.text \
        = ('<a href="http://www.aozora.gr.jp/index_pages/person879.html">芥川</a>の5作目の短編小説。'
           "次の作品『今昔物語集』巻二十九「羅城門登上層見死人盗人語第十八」に題材を取り、"
           "人間のエゴイズムについて作者自身の解釈を加えたものである。")

    # <item><book:writer>要素の追加
    elm_item_writer = ET.SubElement(elm_item, 'book:writer', id="879")
    elm_item_writer.text = "芥川 竜之介"

    # XML文字列に変換
    xml = ET.tostring(elm_rss, 'utf-8')

    # 先頭行に <?xml version="1.0"?> を追加し、整形する
    with minidom.parseString(xml) as dom:
        return dom.toprettyxml(indent="  ")


if __name__ == '__main__':
    rss_str = create_rss()
    print(rss_str)
