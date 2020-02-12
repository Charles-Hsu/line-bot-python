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
    
- 需要 git 上去的檔案： app.py, requirements.txt, Procfile
    
    

參考資料

https://github.com/yaoandy107/line-bot-tutorial
