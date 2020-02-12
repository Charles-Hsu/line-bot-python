#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('EeipgqpO8xgS1Jgq0JByhUBv7KdTN/oW5sNTrY57mj7vDTiF9i+lSpoDKoKzxhTTL2ktLpMsDvF+WSJR79ZtuxI791p87pcdwnoTcPtrGI8NtELAMOqO3CicRq8pIVGDi92ss9yZ0ZE6D6pDR5jorwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0ba16161a671a1534fc456d1155034c9')
# listening /callback Post Request

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# routing
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

@app.route('/')
def index():
    return 'Hello World'

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)