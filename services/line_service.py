from linebot import LineBotApi
from linebot.models import TextSendMessage

class LineService:
    def __init__(self, access_token: str):
        self.line_bot_api = LineBotApi(access_token)
    
    def reply_message(self, reply_token: str, text: str):
        self.line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=text)
        )