import os
import requests

BURNED_URL = os.getenv('BURNED_URL')
MKR_BURN_URL = 'https://makerburn.com'
EXPLORE_URL = os.getenv('EXPLORE_URL')

def system_overview():

    explore = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()
    burned = requests.get(BURNED_URL).json()

    total_dai = burned['dai_total']
    dai_sent = 0
    eth_locked = explore['ethCollateral']
    bat_locked = explore['batCollateral']
    usdc_locked = explore['usdcCollateral']
    eth_price = explore['ethPrice']
    bat_price = explore['batPrice']
    usdc_price = float(explore['usdcPrice'])

    total_collateral_value = eth_locked * eth_price + bat_locked * bat_price + usdc_locked * usdc_price

    apr_eth = (burned['mcd_fee_eth'] ** (60 * 60 * 24 * 365) - 1) * 100
    apr_bat = (burned['mcd_fee_bat'] ** (60 * 60 * 24 * 365) - 1) * 100
    apr_usdc = (burned['mcd_fee_usdc'] ** (60 * 60 * 24 * 365) - 1) * 100

    dsr_apr = (burned['dsr_rate'] ** (60 * 60 * 24 * 365) - 1) * 100
    dai_in_dsr = burned['dai_in_dsr']
    mkr_total = burned['mkr_total']

    eth_perc = eth_locked * eth_price / total_collateral_value * 100
    bat_perc = bat_locked * bat_price / total_collateral_value * 100
    usdc_perc = bat_locked * bat_price / total_collateral_value * 100

    # add -> :dai: Sent (24 hrs): [Pending] | 
    return f'''
Total :dai:: {total_dai:,.1f} | DSR: {dsr_apr:.2f}% | :honey_pot: {dai_in_dsr:,.2f}
Collateral Value Locked: ${total_collateral_value:,.2f} ({total_collateral_value/total_dai*100:.2f}%)
Locked: :eth:: {eth_locked:,.1f} ({eth_perc:.0f}%) | :battoken:: {bat_locked:,.1f} ({bat_perc:.0f}%) | :usdc:: {usdc_locked:,.1f} ({usdc_perc:.0f}%)
Fee: :eth:: {apr_eth:.2f}% | :battoken:: {apr_bat:.2f}% | :usdc:: {apr_usdc:.2f}% | :mkr:: {mkr_total:,.1f}
'''   

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

print(system_overview())
