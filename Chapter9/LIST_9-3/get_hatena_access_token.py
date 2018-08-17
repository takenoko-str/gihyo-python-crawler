"""はてなAPIを利用するためのアクセストークンを取得する."""
import os

from flask import Flask, request, redirect, session
from furl import furl
from requests_oauthlib import OAuth1Session

app = Flask(__name__)
app.secret_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX # 作成しておいたシークレットキー

OAUTH_CONSUMER_KEY = '(OAuth Consumer Keyを入力します)'
OAUTH_CONSUMER_SECRET = '(OAuth Consumer Secretを入力します)'

# リクエストトークン取得用URL
TEMPORARY_CREDENTIAL_REQUEST_URL = 'https://www.hatena.com/oauth/initiate'
# 認証用URL
RESOURCE_OWNER_AUTHORIZATION_URL = 'https://www.hatena.ne.jp/oauth/authorize'
# アクセストークン取得用URL
TOKEN_REQUEST_URL = 'https://www.hatena.com/oauth/token'

# 認証用URLでAPIアクセス許可を実行した後リダイレクトするURL
CALLBACK_URI = 'http://127.0.0.1:5000/callback_page'
SCOPE = {'scope': 'read_public,write_public'}  # 権限


@app.route('/')
def index():
    """リクエストトークンを取得し認証URLにリダイレクトする."""
    # リクエストトークンの取得
    oauth = OAuth1Session(OAUTH_CONSUMER_KEY, client_secret=OAUTH_CONSUMER_SECRET, callback_uri=CALLBACK_URI)
    fetch_response = oauth.fetch_request_token(TEMPORARY_CREDENTIAL_REQUEST_URL, data=SCOPE)

    # セッションに保存する
    session['request_token'] = fetch_response.get('oauth_token')
    session['request_token_secret'] = fetch_response.get('oauth_token_secret')

    # リクエストトークンを使い認証URLを組み立て、認証URLにリダレイクトする
    redirect_url = furl(RESOURCE_OWNER_AUTHORIZATION_URL)
    redirect_url.args['oauth_token'] = session['request_token']
    return redirect(redirect_url.url)


@app.route('/callback_page')
def callback_page():
    """verifierを得て、アクセストークンを取得・表示するためのコールバックページ."""
    # URLパラメーターoauth_verifierを参照してverifierを取得する
    verifier = request.args.get('oauth_verifier')
    # ここまでで得たリクエストトークンとverifierを使ってアクセストークンを取得する
    oauth = OAuth1Session(
                OAUTH_CONSUMER_KEY,
                client_secret=OAUTH_CONSUMER_SECRET,
                resource_owner_key=session['request_token'],
                resource_owner_secret=session['request_token_secret'],
                verifier=verifier)

    access_tokens = oauth.fetch_access_token(TOKEN_REQUEST_URL)
    access_token = access_tokens.get('oauth_token')
    access_secret = access_tokens.get('oauth_token_secret')
    return "アクセストークン: {}, アクセストークン・シークレットキー: {}".format(
            access_token, access_secret)


if __name__ == '__main__':
    app.run(debug=True)
