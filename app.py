from sys import path
from flask import Flask,render_template,abort
import sys,os

from flask import request

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
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
)
import os


# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET=os.getenv("YOUR_CHANNEL_SECRET")

# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

YOUR_CHANNEL_ACCESS_TOKEN=os.getenv("YOUR_CHANNEL_ACCESS_TOKEN")

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)



@app.route("/show-db")
def db_show():
    s=models.create_sesson()
   
    result=s.query(models.UUID_CO2).all()
    result2=s.query(models.UUID_LINE_ID).all()
    result3=s.query(models.UUID_MAIL).all()

    if len(result)==0:
        s.add(models.UUID_CO2(uuid=1234,co2=5000))
        s.commit()
   
    s.close()

    return render_template("idx.html",uuidco2=result,uuid_mail=result3,uuid_line=result2)


@app.route("/")
def root():

    return "<h1>GOOOOOOOD</h1>"

@app.errorhandler(404)
def page_not_found(error):
    ipaddr=request.environ["REMOTE_ADDR"]
    # print(ipaddr)
    return render_template('page_not_found.html',ip=ipaddr), 404





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
import random
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    URI=I.rand_img()
    user_id=event.source.user_id
    
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text="次の問題を解け"))

    line_bot_api.push_message(
        user_id,
        ImageSendMessage(original_content_url=URI,preview_image_url=URI
        ))

if __name__ == '__main__':
    
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", 5000))
    )
