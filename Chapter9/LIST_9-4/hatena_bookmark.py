"""はてなブックマークAPIユーティリティ."""
import requests
from requests_oauthlib import OAuth1

OAUTH_CONSUMER_KEY = '(OAuth Consumer Keyを入力します)'
OAUTH_CONSUMER_SECRET = '(OAuth Consumer Secretを入力します)'
ACCESS_TOKEN = 'アクセストークンを入力します'
ACCESS_SECRET = 'アクセストークン・シークレットキーを入力します'

# ブックマークするURLをPOSTするAPIエンドポイント
BOOKMARK_ENDPOINT = 'http://api.b.hatena.ne.jp/1/my/bookmark'
# はてなのAPIアクセスにはUser-Agentの指定が必須
HEADERS = {'User-Agent': 'auto_hatebu (自分のメールアドレスを入力してください)'}

auth = OAuth1(
        OAUTH_CONSUMER_KEY,
        OAUTH_CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_SECRET,
        signature_type='auth_header')
# OAuth認証やヘッダー情報は毎回同じなのでセッションにしておく
s = requests.Session()
s.auth = auth
s.headers.update(HEADERS)


def bookmark_url(target_url):
    """ブックマークを追加する."""
    return s.post(BOOKMARK_ENDPOINT, data={'url': target_url})


if __name__ == '__main__':
    r = bookmark_url('http://b.hatena.ne.jp/hotentry/it')
    print(r.text)
