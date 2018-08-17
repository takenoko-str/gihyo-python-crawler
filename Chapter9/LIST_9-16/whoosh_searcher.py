import sys

from whoosh_lib import get_or_create_index
from whoosh.qparser import QueryParser


if __name__ == '__main__':
    # インデックスの取得
    ix = get_or_create_index()

    # 検索キーワードの入力プロンプトを表示し、keyword変数へ取り込む
    keyword = input("検索キーワードを入力してください: ")

    # bodyフィールドを対象にkeywordの文字列で検索する
    with ix.searcher() as searcher:
        # キーワードから、スキーマのbodyへの検索クエリオブジェクトを作成
        query = QueryParser("body", ix.schema).parse(keyword)
        # 検索実行
        results = searcher.search(query)
        if not results:
            print('検索結果が見つかりませんでした')
            sys.exit(0)
        print('検索結果が見つかりました')
        for i, r in enumerate(results):
            print("{}: post_url: {}".format(i + 1, r['post_url']))
