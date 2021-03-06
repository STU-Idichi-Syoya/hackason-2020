from sys import path
from flask import Flask,render_template,abort
import sys,os

from flask import request,Response
from linebot.models import messages
from requests.packages.urllib3 import HTTPResponse
from sqlalchemy import exc

sys.path.extend(["models","scripts"])
import models

app = Flask(__name__)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FollowEvent
)
import os


# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET=os.getenv("YOUR_CHANNEL_ACCESS_TOKEN","kj")



# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

YOUR_CHANNEL_ACCESS_TOKEN=os.getenv("YOUR_CHANNEL_SECRET","ok")


line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET )





import database
import mail
@app.route('/co2', methods=['POST'])
def co2():
    message = request.get_json()
    co2=int(message["value"])
    uuid=message["id"]
    database.update_co2(uuid,co2)
    

    if co2 > 1000:
        mail_list=database.get_mail_addr(uuid)
        for adr in mail_list:
            mail.send_alert(adr)
            pass
        
        line_ids=database.get_Line_id(uuid)
        for id in line_ids:
            print(id,type(id))
            try:
                line_bot_api.push_message(
                    id,TextMessage(text="CO2が充満しております。至急換気をお願いします。")
                )
            except:
                print("fail line id-->",id)

    return Response("OK",status=200)

@app.route("/show-db")
def db_show():
    s=models.create_sesson()
   
    result=s.query(models.Place).all()
    result2=s.query(models.Line).all()
    result3=s.query(models.Mail).all()


    return render_template("idx.html",Place=result,uuid_mail=result3,uuid_line=result2)

import json
@app.route("/map")
def query_react():
    ## json
    '''
    {
        "places":[
            {
                # DB と同じだが、IDを省く
                "lat": 緯度
                "lng": 経度
                "name": なまえ
                "avarage": 500~2000とかの乱数？
            },
        ]

    }
    '''
    return json.dumps(database.get_react_map()),200





@app.route('/')
def root():
    return render_template("食堂店舗のご案内｜食堂｜関西大学生活協同組合.html")

@app.route('/demo/k')
def root2():
    return render_template("食堂店舗のご案内｜食堂｜関西大学生活協同組合.html")



@app.errorhandler(404)
def page_not_found(error):
    if request.headers.getlist("X-Forwarded-For"):
       ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
       ip = request.remote_addr
    # print(ipaddr)
    return render_template('page_not_found.html',ip=ip), 404


from flask import Flask, render_template #追加

import random
@app.route('/openapi/<uuid>')
def hello(uuid):
    ppm=database.get_co2(uuid)
    
    # s=""
    if ppm is None:
        ppm=random.randint(200,1500)
    # print(uuid)
    if ppm<1000:
        return render_template("chk.html",ppm=str(ppm))
    else:
        return render_template("tri.html",ppm=str(ppm))



@app.route("/line-callback", methods=['POST'])
def line_call_back():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

import integral as I

user_id_ses={}
user_id_ses_d={}

import random
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # URI=I.rand_img()
    user_id=event.source.user_id
    msg=event.message.text
    
    if msg=="追加":
        user_id_ses[user_id]="uuid wait"
        line_bot_api.push_message(
            user_id,
            TextSendMessage(text="UUIDを入力してください"))

    elif user_id in user_id_ses:
        state=user_id_ses[user_id]
        if state=="uuid wait":
            tmsg="連携しました,もしメールアドレスも登録する場合、\nメールアドレスを入力してください。それ以外は終了と入力してください"
            try:
                database.add_line(msg,user_id)
                user_id_ses_d[user_id]=msg
                user_id_ses[user_id]="mail wait"
            except:
                 tmsg="UUIDを間違えているかサーバ上に存在しません\n入力しなおしてください"
                 import traceback
                 traceback.print_exc()
            line_bot_api.push_message(
                user_id,
                TextSendMessage(text=tmsg))
        elif state=="mail wait":
            tmsg=""
            if "@" in msg :
                database.add_mail(user_id_ses_d[user_id],msg)
                tmsg="登録しました"
            elif "終了" in msg:
                user_id_ses[user_id]="ok"
                tmsg="終了しました"
            else:
                tmsg="有効なメールアドレスを入力してください"

            line_bot_api.push_message(
                user_id,
                TextSendMessage(text=tmsg))
            
    
    # else:
    #     line_bot_api.push_message(
    #         user_id,
    #         TextSendMessage(text="次の問題を解け,または「追加」と入力してください"))

    #     line_bot_api.push_message(
    #         user_id,
    #         ImageSendMessage(original_content_url=URI,preview_image_url=URI
    #         ))






import line_tools


@handler.add(FollowEvent)
def first_add_line(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='このアカウントはCO2通知BOTです。\n連携する場合は\"追加\"と言ってください\n')
    )



def add_line_id_uuid(event):
    user_id=event.source.user_id
    
    line_bot_api.reply_message(
        TextMessage(text="工場出荷番号（UUID）を入力してください")
    )


import flask_cors
flask_cors.CORS(app)

if __name__ == '__main__':
    
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", 5000))
    )
    print(1)