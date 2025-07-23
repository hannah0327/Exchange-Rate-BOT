import requests
from typing import Dict, Optional

class CurrencyService:
    def __init__(self, api_url: str):
        self.api_url = api_url
    
    def get_currency_data(self) -> Optional[Dict]:
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"獲取匯率資料失敗: {e}")
            return None
    
    def convert_currency(self, from_currency: str, to_currency: str) -> Optional[float]:
        data = self.get_currency_data()
        if not data:
            return None
        
        # 處理不同的貨幣轉換邏輯
        pair = f"{from_currency}{to_currency}"
        
        if pair in data:
            return data[pair]['Exrate']
        elif from_currency == 'TWD':
            # TWD 轉其他貨幣需要透過 USD
            usd_rate = data.get('USDTWD', {}).get('Exrate')
            target_rate = data.get(f'USD{to_currency}', {}).get('Exrate')
            if usd_rate and target_rate:
                return target_rate / usd_rate
        elif to_currency == 'TWD':
            # 其他貨幣轉 TWD
            usd_rate = data.get(f'{from_currency}USD')
            if usd_rate:
                twd_rate = data.get('USDTWD', {}).get('Exrate')
                return twd_rate / usd_rate['Exrate']
        
        return None