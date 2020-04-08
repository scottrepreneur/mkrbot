import os
import requests

BURNED_URL = os.getenv('BURNED_URL')
MKR_BURN_URL = 'https://makerburn.com'

def dai_supply():

    burned = requests.get(BURNED_URL).json()

    total_dai = burned['dai_total']
    dai_cap = burned['dai_cap']
    dai_from_eth = burned['dai_from_eth']
    eth_dai_cap = burned['mcd_dai_cap_eth']
    dai_from_bat = burned['dai_from_bat']
    bat_dai_cap = burned['mcd_dai_cap_bat']
    dai_from_usdc = burned['dai_from_usdc']
    usdc_dai_cap = burned['mcd_dai_cap_usdc']
    total_sai = burned['sai_total']
    sai_cap = burned['scd_sai_cap']

    return f'''
All :dai:: {total_dai:,.0f} / {dai_cap/1000000:,}MM ({total_dai/dai_cap*100:.0f}%) | :dai: from :eth:: {dai_from_eth:,.0f} / {eth_dai_cap/1000000:,}MM ({dai_from_eth/eth_dai_cap*100:.0f}%)
:dai: from :battoken:: {dai_from_bat:,.0f} / {bat_dai_cap/1000000:,}MM ({dai_from_bat/bat_dai_cap*100:.0f}%) | :dai: from :usdc:: {dai_from_usdc:,.0f} / {usdc_dai_cap/1000000:,}MM ({dai_from_usdc/usdc_dai_cap*100:.0f}%)
:sai:: {total_sai:,.0f} / {sai_cap/1000000:,}MM ({total_sai/sai_cap*100:.0f}%) | [Check out more details on Makerburn]({MKR_BURN_URL})'''

def dsr_overview():

    dsr = requests.get(BURNED_URL).json()

    dsr_apr = (dsr['dsr_rate'] ** (60 * 60 * 24 * 365) - 1) * 100
    dai_in_dsr = dsr['dai_in_dsr']
    total_dai = dsr['dai_total']


    return f'''
:dai: Savings Rate: {dsr_apr}% | :dai: in DSR: {dai_in_dsr:,.0f}
DSR Utilization: {dai_in_dsr/total_dai*100:.2f}% | Total :dai:: {total_dai:,.0f}
'''
