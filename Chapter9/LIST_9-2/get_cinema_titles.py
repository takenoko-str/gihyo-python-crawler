"""Chromeのヘッドレスモードで映画ランキングのタイトルをスクレイピングする."""
import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# ロガーのセットアップ
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


# Chrome Driverの実行オプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

chrome_driver_path = ('/Users/peketamin/python/chromedriver')


if __name__ == '__main__':
    try:
        # Chromeをヘッドレスモードで呼び出す
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

        # スクレイピング対象URLの指定
        target_url = "http://0.0.0.0:8000/vue_sample.html"
        # ヘッドレスモードのChromeでスクレイピング対象URLを開く
        driver.get(target_url)

        # 内部でAjaxを利用した処理がある場合、その処理が終わるのを待つため間隔を空ける
        time.sleep(2)

        # 映画タイトル要素をCSSセレクタを指定して抽出
        title_elms = driver.find_elements_by_css_selector(".cinema_title")

        # 抽出された要素ごとに、タグで挟まれたテキストを表示
        for i, t in enumerate(title_elms):
            print(i+1, t.text)
    except Exception as e:
        # 例外エラー時はスタックトレースを表示する
        logger.exception(e)
    finally:
        # 例外エラーでプログラムが終了した後にChromeプロセスが残ってしまうのを防ぐ
        driver.close()
