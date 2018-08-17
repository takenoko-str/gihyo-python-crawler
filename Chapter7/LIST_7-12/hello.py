from flask import Flask
app = Flask(__name__)  # Flaskインスタンスの作成

# トップページ / にアクセスした際に実行される関数
@app.route("/")
def hello():  # 関数名は任意
    return "Hello World!"
