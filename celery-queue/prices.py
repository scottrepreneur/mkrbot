import os
import requests

EXPLORE_URL = os.getenv('EXPLORE_URL')

last_price = {
    'eth': 0,
    'bat': 0,
    'usdc': 0,
    'wbtc': 0
}

def price_overview():

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()

    eth_price = float(prices['ethPrice'])
    next_eth_price = float(prices['ethFuturePrice'])
    bat_price = float(prices['batPrice'])
    next_bat_price = float(prices['batFuturePrice'])
    usdc_price = float(prices['usdcPrice'])
    next_usdc_price = float(prices['usdcFuturePrice'])

    return f'''
> :eth: Next: ${next_eth_price:.2f} | Current: ${eth_price:.2f}
> :battoken: Next: ${next_bat_price:.2f} | Current: ${bat_price:.2f}
> :usdc: Next: ${next_usdc_price:.2f} | Current: ${usdc_price:.2f}
> :mkr: Next: [Pending] | Current: [Pending]
'''

def price_update():
    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()

    next_eth_price = float(prices['ethFuturePrice'])
    next_bat_price = float(prices['batFuturePrice'])
    next_usdc_price = float(prices['usdcFuturePrice'])

    return f'''
:eth:: ${next_eth_price:.2f} | :battoken:: ${next_bat_price:.3f} | :usdc:: ${next_usdc_price:.2f} | :dai:: [Pending] | :mkr:: [Pending]
'''

def eth_price():

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()

    eth_price = float(prices['ethPrice'])
    next_eth_price = float(prices['ethFuturePrice'])

    return f'''
> :eth: Next: ${next_eth_price:.2f} | Current: ${eth_price:.2f}
'''

def bat_price():

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()

    bat_price = float(prices['batPrice'])
    next_bat_price = float(prices['batFuturePrice'])

    return f'''
> :battoken: Next: ${next_bat_price:.2f} | Current: ${bat_price:.2f}
'''

def usdc_price():

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()

    usdc_price = float(prices['usdcPrice'])
    next_usdc_price = float(prices['usdcFuturePrice'])

    return f'''
> :usdc: Next: ${next_usdc_price:.2f} | Current: ${usdc_price:.2f}
'''
