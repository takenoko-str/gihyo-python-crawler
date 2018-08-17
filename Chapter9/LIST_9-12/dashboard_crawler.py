"""Tumblrダッシュボードをクロールする."""
import json

import pytumblr

# OAuth認証を使ったAPIクライアントオブジェクトを作成する
client = pytumblr.TumblrRestClient(
  # 下記にコードサンプルからコピーしてきたトークンを貼り付けてください
  'XXXXXXXXXX',
  'XXXXXXXXXX',
  'XXXXXXXXXX',
  'XXXXXXXXXX'
)


def get_dashboard_posts():
    """ダッシュボードの投稿を取得する."""
    return client.dashboard(type='text')


if __name__ == '__main__':
    dashboard_posts = get_dashboard_posts()
    print(json.dumps(dashboard_posts, ensure_ascii=False))

