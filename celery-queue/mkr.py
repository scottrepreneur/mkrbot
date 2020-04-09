import os
import requests

BURNED_URL = os.getenv('BURNED_URL')

def mkr_burned():

    burned = requests.get(BURNED_URL).json()

    total_mkr = burned['mkr_total']
    mkr_burned = burned['mkr_burned']
    mkr_burner = burned['mkr_in_burner']
    mkr_price = burned['mkr_price']

    return f''':mkr: Total Supply: {total_mkr:,.2f} | :mkr: Price: ${mkr_price:.2f}
:mkr: Burned: {mkr_burned:,.2f} | :mkr: in Burner: {mkr_burner:,.2f}'''

def stability_fees():

    fees = requests.get(BURNED_URL).json()

    apr_eth = (fees['mcd_fee_eth'] ** (60 * 60 * 24 * 365) - 1) * 100
    apr_bat = (fees['mcd_fee_bat'] ** (60 * 60 * 24 * 365) - 1) * 100
    apr_usdc = (fees['mcd_fee_usdc'] ** (60 * 60 * 24 * 365) - 1) * 100

    return f'''*Stability Fees* 
Annual Percentage Rate | :eth:: {apr_eth:.2f}%
:battoken:: {apr_bat:.2f}% | :usdc:: {apr_usdc:.2f}%'''
