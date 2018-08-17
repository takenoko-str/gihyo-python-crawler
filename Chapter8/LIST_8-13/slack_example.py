import requests

WEBHOOK_URL = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/xxxxxxxxxxxxxxxxxxxxxxxx'


def notify_to_slack(text):
    data = {"text": text}
    r = requests.post(WEBHOOK_URL, json=data)
    r.raise_for_status()


if __name__ == '__main__':
    notify_to_slack("@me pythonからの投稿テストです.")

