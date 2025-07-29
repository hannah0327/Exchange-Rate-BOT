# LINE Bot 匯率查詢系統
---

## 專案簡介

一個使用 Flask + LINE Messaging API 開發的匯率查詢機器人，支援多種貨幣轉換，採用模組化架構設計，易於維護和擴展。

## 專案功能
- LINE Bot 即時訊息回應
- 支援 6 種貨幣轉換 (USD/TWD/EUR/JPY)
- 模組化架構設計 (MVC 模式)

## Demo影片
https://github.com/user-attachments/assets/86b80508-9a4a-40d1-83e6-82fbfe47e692

---

## 快速開始
以下說明將引導你在本地機器上搭建和運行此專案，以便進行開發和測試。  

### 環境需求
你的系統上需要安裝與註冊以下軟體：
- Python 3.8+
- LINE Developer Account
- ngrok

### 安裝步驟
### 1. 複製專案：
```bash
git clone <你的儲存庫網址>
cd currency_bot
```

### 2.建立虛擬環境並安裝相依套件：
```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows)
venv\Scripts\activate

# 啟動虛擬環境 (macOS/Linux)
source venv/bin/activate

pip install -r requirements.txt
```

### 3.設定環境變數：
建立 .env 檔案並填入你的 LINE Bot 資訊：
```bash
LINE_CHANNEL_SECRET=你的_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=你的_channel_access_token
```

### 4.執行應用程式：
```bash
python app.py
```

### 5.設定外部連線測試 (使用 ngrok)：
安裝並啟動 ngrok 來建立外部連線：
```bash
# 安裝 ngrok (若尚未安裝)
# 前往 https://ngrok.com/ 下載

# 開啟外部連線
ngrok http 5000
```
複製 ngrok 提供的 HTTPS 網址，並設定到 LINE Developers Console：
```bash
https://abcd1234.ngrok.io/callback
```

---

## 使用說明
### 支援的查詢指令
| 指令         | 說明           | 匯率資訊                         |
|--------------|----------------|----------------------------------|
| @USD to TWD  | 美元兌台幣     | 美元 USD 兌台幣 TWD：1:31.2500  |
| @USD to EUR  | 美元兌歐元     | 美元 USD 兌歐元 EUR：1:0.9200   |
| @USD to JPY  | 美元兌日幣     | 美元 USD 兌日幣 JPY：1:149.8000 |
| @TWD to USD  | 台幣兌美元     | 台幣 TWD 兌美元 USD：1:0.0320   |
| @TWD to EUR  | 台幣兌歐元     | 台幣 TWD 兌歐元 EUR：1:0.0294   |
| @TWD to JPY  | 台幣兌日幣     | 台幣 TWD 兌日幣 JPY：1:4.7920   |


### 本地測試流程
1. 執行 Flask 應用程式 (python app.py)
2. 開啟新的終端機視窗，執行 ngrok http 5000
3. 複製 ngrok 提供的 HTTPS 網址 (例如: https://abcd1234.ngrok.io)
4. 到 LINE Developers Console 設定 Webhook URL: https://abcd1234.ngrok.io/callback
5. 加入 LINE Bot 為好友進行測試
6. 發送對應指令應可獲得即時匯率資訊

