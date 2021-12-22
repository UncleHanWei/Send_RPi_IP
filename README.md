# Send Raspberry IP

## 關於
為了避免每次想透過 SSH 使用 RPi 都要想盡辦法取得 ip，因此寫了這樣一支程式。
透過 Telegram 將 ip 發送給自己的帳號，更便利的取得 RPi 的 ip。

## 套件
- telethon
    - `pip3 install telethon`

## 使用
### Step 1 : 註冊應用並取得操作資訊
- 登入 my.telegram.org
![](https://i.imgur.com/cLjCFRj.png)

- 選擇 API development tools
![](https://i.imgur.com/ktWcc8S.png)

- 註冊應用後便會進入應用的設定頁面
![](https://i.imgur.com/bXereSF.png)


## Step 2 : 修改程式
- 將程式中的 `api_id`、`api_hash` 替換成從 my.telegram.org 取得的值(上圖中黑線塗掉的部分)

## Step 3 : 首次執行登入
- 輸入電話號碼
    - 第一次執行程式時，因為尚未建立 session，需要輸入電話號碼，電話號碼的格式以 + 開頭(台灣的話為 +886)
- 輸入登入驗證碼
    - 輸入電話號碼後會收到 telegram 寄送的驗證碼
    - 輸入驗證碼後，若無錯誤即可查看 Telegram，檢查是否收到 IP

