"""filmテーブル用RESTful API."""
from flask import Flask, abort
from flask_restful import Api, Resource, reqparse

# db.py から Filmテーブルモデル用のクラスをインポート
from db import Film

app = Flask(__name__)

# RESTful API 用インスタンスの作成
api = Api(app)


# 単一のアイテムを表示する用
class FilmItem(Resource):
    """特定のFilm."""

    def get(self, film_id):
        """GET実行時のアクション."""
        try:
            # filmテーブルからfilm_id を検索してデータベースから取得する
            film = Film.get(Film.film_id == film_id)
        except Film.DoesNotExist:
            # 見つからなかった場合は処理を中断して 404 を返す
            abort(404, description="Film not found.")

        # 辞書形式でreturnすると、自動的にJSONに変換される
        return film.to_dict()


# 複数のアイテムを一覧で表示する用
class FilmList(Resource):
    """Filmリスト."""

    # 1ページあたりのアイテム数
    ITEMS_PER_PAGE = 5

    def __init__(self, *args, **kwargs):
        """GETで受け取るパラメーター用のparserを作る."""
        self.parser = reqparse.RequestParser()

        # これにより ?page=2 のようにページ数を指定できるようにする
        self.parser.add_argument('page', type=int, default=1)
        super().__init__(*args, **kwargs)

    def get(self):
        """GET実行時のアクション."""
        # GET で受け取ったパラメーター (例: ?page=2) をパースする
        args = self.parser.parse_args()

        # filmテーブルから5件ずつ、pageパラメーターに応じてアイテムを取得する
        films = Film.select()\
            .order_by(Film.film_id)\
            .paginate(args['page'], self.ITEMS_PER_PAGE)  # ページング処理

        # 辞書形式でreturnすると、自動的にJSONに変換される
        return [film.to_dict() for film in films]


# どのURL形式で、どの処理が実行されるかを割り当てる
api.add_resource(FilmItem, '/film/<int:film_id>')
api.add_resource(FilmList, '/films')

if __name__ == '__main__':
    # Webサーバーの実行
    app.run(debug=True)
