import smtplib

from email.message import EmailMessage

FROM = '自分のメールアドレスを入力してください'


def mail(to, subject, body=None):
    msg = EmailMessage()
    msg['To'] = to
    msg['Subject'] = subject
    msg['From'] = FROM
    if body is None:
        raise ValueError("本文が空です")
    else:
        msg.set_content(body)

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)


if __name__ == '__main__':
    mail('自分のメールアドレスを入力してください', "メール送信テストです", "このメールはPythonから送信されました.")
