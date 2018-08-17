import os

from whoosh import index
from whoosh.fields import Schema, ID, TEXT, NGRAM


# インデックスデータを保存するディレクトリの指定
INDEX_DIR = "indexdir"

# インデックス用スキーマの定義
schema = Schema(
    # インデックスのユニークなIDとして投稿データのURLを使う
    post_url=ID(unique=True, stored=True),
    # 本文をNGRAMでインデックス化する
    body=NGRAM(stored=True),
)


def get_or_create_index():
    # インデックス用ディレクトリがなければ作成する
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        # インデックス用ファイルの作成
        ix = index.create_in(INDEX_DIR, schema)
        return ix

    # 既にインデックスディレクトリがあれば
    # 既存のインデックスファイルを開く
    ix = index.open_dir(INDEX_DIR)
    return ix
