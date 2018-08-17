import csv
from itertools import islice 

# ファイルオブジェクトとしてCSVファイルを開く
with open('gaku-mg1642.csv', 'r', encoding='shift-jis') as csvFile:
  # readerオブジェクトを取得する
  dataReader = csv.reader(csvFile)

  # 1行ごとリストで取得することができるので8行目からコンソールに出力して確認する
  for row in islice(dataReader,7,None):
    print(row[1]) # 2列目だけ出力するように修正する

