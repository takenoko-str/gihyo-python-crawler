import requests
import lxml.html

# HTMLソースを得る
r = requests.get("http://www.shoeisha.co.jp/book/detail/9784798146072")
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

# XPathを指定して該当する要素のリストを得る
titleH1 = root.xpath("/html/body/div[1]/section/h1")

# リストの1番目のテキストを表示する
print(titleH1[0].text)

# CSSセレクターで該当する要素のリストを得る
qaA = root.cssselect("#qa > p > a")

## forループで回して取得した要素のhref要素を表示する
for aTag in qaA:
  print(aTag.attrib["href"])