#!/bin/bash
function main_command() {
    echo 'コマンドを実行しています...';
    sleep 30;
}

# プロセスIDを書き込むファイル名
PIDFILE=/tmp/lock_example.pid

# もしプロセスIDを書き込むファイルが存在していれば
if [ -f $PIDFILE ];then
    # プロセスIDを変数 PID へ格納
    PID=$(cat $PIDFILE)

    # ps コマンドで変数PIDのプロセスIDを持つプロセスが存在するか確認する
    ps -p $PID > /dev/null 2>&1;

    # 上記コマンドの実行結果が 0 ならばプロセスが存在する
    if [ $? -eq 0 ];then
        echo "既に起動しています. PID: $PID";
        exit 1;
    # そうでない場合は、プロセスIDを書き込んだファイルは存在するがプロセスが存在していない
    else
        echo "$PIDFILE は存在しますがプロセスは起動していません.";
        echo "状況を確認して問題がなければ $PIDFILE を削除して再実行してください.";
        exit 1;
    fi
fi

# プロセスIDをファイル名 PIDFILE のファイルに書き込む
echo $$ > $PIDFILE;
echo "プロセスを起動します. プロセスID: $(cat $PIDFILE)";
# main_command を実際に起動したいコマンドに置き換えてください
main_command;
# コマンドの実行が終わったらプロセスIDを書き込んだファイルも削除する
rm $PIDFILE;
