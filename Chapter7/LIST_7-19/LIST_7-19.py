import requests
from janome.tokenizer import Tokenizer
from bs4 import BeautifulSoup
from wordcloud import WordCloud

# HTMLの取得
url = 'http://www.aozora.gr.jp/cards/000879/files/42_15228.html'
r = requests.get(url, timeout=10)

# パース
soup = BeautifulSoup(r.content, 'lxml')

# 本文の抽出
text_elm = soup.find('div', attrs={'class': 'main_text'})
# ルビ要素を削除
[e.extract() for e in text_elm.select('rt')]

# ルビが削除されたテキストを取得
text = text_elm.text

# ストップワードの取得
stop_word_url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
r_stopword = requests.get(stop_word_url, timeout=10)
stop_words = r_stopword.text.split()

# 単語に分割
t = Tokenizer()
words = []
for token in t.tokenize(text):
    if token.part_of_speech.split(',')[0] == '名詞' and token.surface not in stop_words:
        words.append(token.surface)

# wordcloudオブジェクトの作成
font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'
wordcloud = WordCloud(background_color="white", font_path=font_path, regexp=r"\w+").generate(" ".join(words))

# グラフ出力
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
