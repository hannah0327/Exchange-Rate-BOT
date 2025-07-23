CURRENCY_COMMANDS = {
    '@USD to TWD': {
        'api_key': 'USDTWD',
        'calculation': lambda data: data['USDTWD']['Exrate'],
        'description': '美元 USD 兌台幣 TWD'
    },
    '@USD to EUR': {
        'api_key': 'USDEUR', 
        'calculation': lambda data: data['USDEUR']['Exrate'],
        'description': '美元 USD 兌歐元 EUR'
    },
    '@USD to JPY': {
        'api_key': 'USDJPY',
        'calculation': lambda data: data['USDJPY']['Exrate'], 
        'description': '美元 USD 兌日幣 JPY'
    },
    '@TWD to USD': {
        'api_key': 'USDTWD',
        'calculation': lambda data: 1/data['USDTWD']['Exrate'],
        'description': '台幣 TWD 兌美元 USD'
    },
    '@TWD to EUR': {
        'api_key': ['USDEUR', 'USDTWD'],
        'calculation': lambda data: data['USDEUR']['Exrate']/data['USDTWD']['Exrate'],
        'description': '台幣 TWD 兌歐元 EUR'
    },
    '@TWD to JPY': {
        'api_key': ['USDJPY', 'USDTWD'], 
        'calculation': lambda data: data['USDJPY']['Exrate']/data['USDTWD']['Exrate'],
        'description': '台幣 TWD 兌日幣 JPY'
    }
}

HELP_MESSAGE = '請輸入查詢代號@USD to TWD:USDTWD @USD to EUR:USDEUR @USD to JPY:USDJPY @TWD to USD:TWDUSD @TWD to EUR:TWDEUR @TWD to JPY:TWDJPY'