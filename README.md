# line-bot-python

參考這篇 [python寫Line Bot必要的2個條件 手把手教學](https://shareboxnow.com/line-bot-python-part-2/#i) 紀錄一些小細節 

#### 到 Heroku 建立一個專案 

    linebot4service
    
#### 在 Line 建立一個 Bot

https://developers.line.biz/console/provider/1653848175

在 Messaging API 內取得 Channel access token 

![](https://github.com/Charles-Hsu/line-bot-python/blob/master/Channel%20access%20token.png)

#### Messaging API settings

    Auto-reply messages Disable
    Use webhook
    
#### Basic settings

![](https://github.com/Charles-Hsu/line-bot-python/blob/master/Channel%20secret.png)

#### 連接 git 資料夾與 Heroku

    $ heroku git:remote -a {HEROKU_APP_NAME}
    $ git add .
    $ git commit -m "init"
    $ git push heroku master
    
- 需要 git 上去的檔案： app.py, requirements.txt, Procfile, 不然會有 error

![](https://github.com/Charles-Hsu/line-bot-python/blob/master/heroku_push_error.png)

    $ heroku logs

這時候到 Line 加入朋友後, 就會有基本的回應, 雖然在 Verify callback 會有沒有成功傳回200的錯誤訊息 (以後再來處理)
![](https://github.com/Charles-Hsu/line-bot-python/blob/master/webhook_other_than_200.png)
    
<img src="https://github.com/Charles-Hsu/line-bot-python/blob/master/line_bot_screen_shoot_1.jpg" width="240">
    
#### 取得 User ID

https://developers.line.biz/console/channel/1653848180

![](https://github.com/Charles-Hsu/line-bot-python/blob/master/Line_Bot_User_ID.png)

點選 Messaging API, 在 Basic Setting 頁面最下方就有 Your user ID 可以選, 複製貼上, 等一下會用到

![](https://github.com/Charles-Hsu/line-bot-python/blob/master/Line_Bot_Basic_Setting.png)

依照步驟做之後, 在 webhook 的位址填上 https://linebot4service.herokuapp.com/push_function, 這時候就可以發送訊息了

<img src="https://github.com/Charles-Hsu/line-bot-python/blob/master/line_bot_screen_shoot_2.jpg" width="240">

參考資料

https://github.com/yaoandy107/line-bot-tutorial
