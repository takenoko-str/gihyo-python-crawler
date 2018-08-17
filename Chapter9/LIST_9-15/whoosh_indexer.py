import os
import sys
import time

import w3lib.html

from dashboard_crawler import get_dashboard_posts

from whoosh_lib import get_or_create_index


if __name__ == '__main__':
    # インデックスハンドラの取得
    ix = get_or_create_index()

    # インデックス書き込み用writerオブジェクトの作成
    writer = ix.writer()

    # ダッシュボードの投稿を取得する
    dashboard_posts = get_dashboard_posts()

    # 投稿データのインデクシングを行う
    for post in dashboard_posts['posts']:
        writer.update_document(
            post_url=post['post_url'],
            # インデックス対象の文章からHTMLタグを取り除く
            body=w3lib.html.remove_tags(post['body']),
        )

    # インデックス書き込みのコミット
    writer.commit()
