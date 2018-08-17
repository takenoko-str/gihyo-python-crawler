import datetime

import requests

from kanazawa_art_db import Event

# イベント情報JSON提供URL
EVENTS_URL = 'http://www.kanazawa-arts.or.jp/event-all.json'
# Slack Webhook API 用 URL
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'


TIMEOUT = 10


def notify_to_slack(text):
    """Slack通知用."""
    data = {"text": text, "link_names": 1}
    requests.post(SLACK_WEBHOOK_URL, json=data)


def parse_date(date_str):
    if not date_str:
        return None
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')


def format_date(date):
    if not date:
        return "不明"
    return date.strftime('%Y年%m月%d日')



def crawl_kanazawa_art_events():
    """イベントをクロール."""

    # イベント情報のJSONを取得
    r = requests.get(EVENTS_URL, timeout=TIMEOUT)

    # JSONをPythonの辞書型に変換する
    events = r.json()

    # 新着イベント格納用リスト
    new_events = []
    for event in events['items']:
        # イベントのリンクを抽出
        link = event.get('link', '')

        # イベントの名前を抽出
        name = event.get('title', '')

        # イベントの概要文を抽出
        description = event.get('description')

        # イベントの開催期間を抽出
        date_from = event.get('date_from')
        date_to = event.get('date_to')

        # イベントオブジェクトの作成
        event = Event(
            name=name,
            url=link,
            description=description,
            date_from=parse_date(date_from),
            date_to=parse_date(date_to),
        )

        # データベースに同じイベントがあるかを確認
        if not Event.exists(link):  # なければ
            event.save()  # データベースに保存
            new_events.append(event)

    # 新着イベントがなければ終了
    if not new_events:
        return

    # 新着イベントがあれば、メッセージを作りSlackに通知する
    # メッセージヘッダ
    message_header = "@channel 新着イベントがありました.\n"

    # イベント情報メッセージ格納用
    messages = []

    # 新着イベントリストからイベントメッセージを作成
    for event in new_events:
        message = "*{}*\n{}\n{}\n開催期間: {} 〜 {}".format(
            event.name,
            event.url,
            event.description,
            format_date(event.date_from),
            format_date(event.date_to),
        )
        messages.append(message)

    # メッセージを一つにまとめる
    full_message = message_header + "\n".join(messages)
    notify_to_slack(full_message)


if __name__ == '__main__':
    crawl_kanazawa_art_events()
