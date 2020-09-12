
## written by カルロス

import smtplib

from email.mime.text import MIMEText
from email.utils import formatdate

def create_message(to_email,from_email,message,subject,charset): #メッセージ作成
    msg = MIMEText(message, 'plain', charset)
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    msg['Date'] = formatdate(localtime=True)
    return msg

def send_mail(to_email,from_email,account,password,msg): #メッセージ送信
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(account, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.login(account, password)
    server.close()

account = "turing.test50@gmail.com" #アカウント名
password = "turing53" #パスワード

from_email = "turing.test50@gmail.com" #FROM

charset = 'ISO-2022-JP' #文字コード
subject = "【危険】CO2ついて"  # 件名
message = "CO2が充満しております。至急換気をお願いします。"  # メール本文

msg = create_message(to_email, from_email, message, subject, charset)

send_mail(to_email, from_email, account, password, msg)

def send_alert(to,from=from_email,msg=message,account=account,subject=subject):
    
    msg = create_message(to_email, from_email, message, subject, charset)
    send_mail(to_email, from_email, account, password, msg)

