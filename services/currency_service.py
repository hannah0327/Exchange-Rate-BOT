import requests
from typing import Dict, Optional

class CurrencyService:
    def __init__(self, api_url: str):
        self.api_url = api_url
    
    def get_currency_data(self) -> Optional[Dict]:
        """獲取匯率資料"""
        try:
            resp = requests.get(self.api_url)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            print(f"獲取匯率資料失敗: {e}")
            return None