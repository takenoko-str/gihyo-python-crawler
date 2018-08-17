import datetime
from hashlib import sha256

import peewee

# Sqliteデータベースファイルの作成
db = peewee.SqliteDatabase('kanazawa_art_events.db')


class Event(peewee.Model):
    """イベント情報用テーブルモデル."""
    name = peewee.CharField()
    url = peewee.CharField()
    description = peewee.CharField()
    date_from = peewee.DateTimeField()
    date_to = peewee.DateTimeField()
    url_hash = peewee.CharField(unique=True)

    # 無指定の場合、現在日時が入るようにする
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    updated_at = peewee.DateTimeField()

    def save(self, *args, **kwargs):
        # イベントの保存時の日時を入れる
        self.updated_at = datetime.datetime.now()
        # self.urlからハッシュを計算し、self.url_hashに入れる
        self.url_hash = sha256(self.url.encode()).hexdigest()
        super().save(*args, **kwargs)

    @classmethod
    def exists(cls, url):
        """同じイベントが既にデータベースに保存されているかの確認用メソッド."""
        url_hash = sha256(url.encode()).hexdigest()
        return cls.select().where(cls.url_hash == url_hash).exists()

    class Meta:
        database = db


if __name__ == '__main__':
    # コマンド実行時の引数でイベントデータベーステーブルの作成と削除ができるようにする
    import argparse
    parser = argparse.ArgumentParser()
    # イベントテーブル作成用コマンド引数の追加
    parser.add_argument('--create-table', action='store_true')
    # イベントテーブル削除用コマンド引数の追加
    parser.add_argument('--drop-table', action='store_true')
    args = parser.parse_args()

    # --create-tableがコマンド引数に指定された場合
    if args.create_table:
        # イベント格納用テーブルを作成してコマンドを終了する
        Event.create_table()
        parser.exit('Event 用テーブルを作成しました.')
    # --drop-tableがコマンド引数に指定された場合
    if args.drop_table:
        # イベント格納用テーブルを削除してコマンドを終了する
        Event.drop_table()
        parser.exit('Event 用テーブルを削除しました.')

    # コマンド引数がない場合はメッセージを表示して終了する
    parser.exit('何もしませんでした.')
