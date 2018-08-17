from flask import Flask

import flask_admin
from flask_admin.contrib import peewee as flask_admin_peewee

import peewee

import aozora_bunko_db


app = Flask(__name__)

# シークレットキーの設定
app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class WriterAdmin(flask_admin_peewee.ModelView):
    """writersテーブル管理画面用クラス."""
    column_display_pk = True
    column_sortable_list = ('id', 'name', 'is_active')
    column_filters = column_sortable_list
    column_editable_list = ('name', 'is_active')
    form_columns = column_sortable_list

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.save(force_insert=True)


@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


if __name__ == '__main__':
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    # 管理画面用オブジェクトの作成
    admin = flask_admin.Admin(app, name='Example: Peewee')

    # writersテーブル用管理画面の追加
    admin.add_view(WriterAdmin(aozora_bunko_db.Writer))

    app.run(debug=True)
