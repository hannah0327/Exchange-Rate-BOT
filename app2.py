from flask import Flask, request, abort
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from config import Config
from services.currency_service import CurrencyService
from services.line_service import LineService
from handlers.message_handler import MessageHandler

app = Flask(__name__)

# 初始化服務
line_service = LineService(Config.LINE_CHANNEL_ACCESS_TOKEN)
currency_service = CurrencyService(Config.CURRENCY_API_URL)
message_handler = MessageHandler(line_service, currency_service)
webhook_handler = WebhookHandler(Config.LINE_CHANNEL_SECRET)

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        webhook_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@webhook_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_handler.handle_text_message(event)

if __name__ == '__main__':
    app.run(debug=True)