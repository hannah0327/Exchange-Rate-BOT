from linebot.models import MessageEvent, TextMessage
from services.currency_service import CurrencyService
from services.line_service import LineService
from utils.constants import CURRENCY_COMMANDS, HELP_MESSAGE

class MessageHandler:
    def __init__(self, line_service: LineService, currency_service: CurrencyService):
        self.line_service = line_service
        self.currency_service = currency_service
    
    def handle_text_message(self, event: MessageEvent):
        input_text = event.message.text
        
        if input_text == '@查詢匯率':
            self.line_service.reply_message(event.reply_token, HELP_MESSAGE)
            return
        
        if input_text in CURRENCY_COMMANDS:
            currency_data = self.currency_service.get_currency_data()
            if not currency_data:
                self.line_service.reply_message(
                    event.reply_token, 
                    "抱歉，無法獲取匯率資料，請稍後再試"
                )
                return
            
            command_info = CURRENCY_COMMANDS[input_text]
            try:
                rate = command_info['calculation'](currency_data)
                message = f"{command_info['description']}：1:{rate}"
                self.line_service.reply_message(event.reply_token, message)
            except (KeyError, ZeroDivisionError) as e:
                self.line_service.reply_message(
                    event.reply_token,
                    "抱歉，匯率計算發生錯誤，請稍後再試"
                )