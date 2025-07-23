import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
    CURRENCY_API_URL = 'https://tw.rter.info/capi.php'