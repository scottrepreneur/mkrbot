import os
import requests

BURNED_URL = os.getenv('BURNED_URL')

def mkr_burned():

    burned = requests.get(BURNED_URL).json()

    total_mkr = burned['mkr_total']
    mkr_burned = burned['mkr_burned']
    mkr_burner = burned['mkr_in_burner']
    mkr_price = burned['mkr_price']

    return f'''MKR Total Supply: {total_mkr:,.2f} | MKR Price: ${mkr_price:.2f}
MKR Burned: {mkr_burned:,.2f} | MKR in Burner: {mkr_burner:,.2f}'''
