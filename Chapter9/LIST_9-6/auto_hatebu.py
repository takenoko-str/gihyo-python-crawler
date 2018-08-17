"""機械学習の人気エントリを自動的にブックマークする."""
import datetime
import logging
import time

import feedparser
import requests

from hatena_bookmark import bookmark_url

# ロガーのセットアップ
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# 機械学習タグの付いたブックマーク数が100以上のエントリが得られるフィードURL
FEED_URL = 'http://b.hatena.ne.jp/search/tag?safe=on&q=%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92&mode=rss&users=100'
TIMEOUT = 10


def extract_links():
    """フィードからブックマークURLリストを抽出する."""
    # フィードの内容を取得する
    r = requests.get(FEED_URL, timeout=TIMEOUT)

    # フィードのXMLをfeedparserでパースする
    f = feedparser.parse(r.content)

    # 現在時刻から見て1日前の日付を計算する
    yesterday = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)

    # ブックマーク対象URL格納用変数
    links = []

    # フィード内のエントリを1件ずつ取り出す
    for entry in f.entries:
        # エントリが登録された日時を取得し、datetime.datetime型に変換する
        entry_updated_date = datetime.datetime(
            *entry.updated_parsed[:6],
            tzinfo=datetime.timezone.utc
        )
        # 前日分のエントリのリンクのみ抽出し、linksリストに追加する
        if entry_updated_date.date() == yesterday:
            links.append(entry.link)
    return links


if __name__ == '__main__':
    # ブックマーク対象のURLをはてなブックマークのフィードから取得する
    links = extract_links()

    # ブックマーク対象のURLを1件ずつ処理する
    for link in links:
        try:
            # はてなブックマークAPIを使ってブックマークする
            r = bookmark_url(link)

            # 連続したリクエストでAPIサーバーに負荷を与えないように間隔を空ける
            time.sleep(1)

            # ブックマークのリクエストでAPIから正常な応答が無かった場合、例外を発生させる
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            # APIリクエストにおいて例外が発生したらログに例外が起きたブックマーク対象のURLを出力する
            # 例外内容も出力する
            logger.error('requested url: {}, e:{}'.format(r.url, e))
        else:
            # 例外が起きなかった場合、ブックマークに成功したURLをログに出力する
            # はてなブックマーク上でのURLも出力する
            logger.info('bookmarked url: {}, permalink: {}'.format(r.url, r.json()['permalink']))
