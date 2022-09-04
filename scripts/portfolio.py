import requests
import json
import os
from enum import Enum, auto
import math


class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    p = get_portfolio()
    print_portfolio(p)

def save_portfolio(p):
    with open('portfolio.json', 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=4)
def get_portfolio():
    with open('portfolio.json') as json_file:
        data = json.load(json_file)
    return data

def print_main_portfolio(s, a, eth):
    total = 0
    for k in a['asset']:
        total += a['asset'][k]
    print_statements = []
    print_statements.append(colors.BOLD + "MAIN" + colors.ENDC)

    max_len_token = max(list(map(lambda x: len(x), {**a['asset'], **a['debt']}.keys())))
    print_statements.append(colors.UNDERLINE + "ASSETS" + colors.ENDC)
    for k in a['asset']:
        if a['asset'][k] == 0: continue
        text = f"{k}: {(max_len_token+1-len(k))*' '}{colors.GREEN}{round(a['asset'][k]/eth, 3)}Ξ{colors.ENDC}"
        text = f"{text}{' '*(28-len(text))}{int(a['asset'][k]*100/total)}%"
        print_statements.append(text)
    if len(a['debt']) > 0: print_statements.append(colors.UNDERLINE + "DEBT" + colors.ENDC)
    for k in a['debt']:
        if a['debt'][k] == 0: continue
        text = f"{k}: {(max_len_token-len(k))*' '}{colors.RED}-{round(a['debt'][k]/eth, 3)}Ξ{colors.ENDC}"
        print_statements.append(text)
        
    for k in a['debt']:
        total -= a['debt'][k]
    print_statements.append(f"TOTAL: {round(total/eth, 3)}Ξ")
    return print_statements

def print_trade_portfolio(s, trade, play, eth):
    
    total = 0
    for k in trade['asset']:
        total += trade['asset'][k]
    for k in play['asset']:
        total += play['asset'][k]
        
    print_statements = []
        
    print_statements.append(colors.BOLD + "FUN" + colors.ENDC)
    for k in play['asset']:
        if play['asset'][k] == 0: continue
        text = f"{k}: {(5-len(k))*' '}{colors.GREEN}{round(play['asset'][k]/eth, 3)}Ξ{colors.ENDC}"
        text = f"{text}{' '*(28-len(text))}{int(play['asset'][k]*100/total)}%"
        print_statements.append(text)
    print_statements.append(colors.BOLD + "TRADE" + colors.ENDC)
    for k in trade['asset']:
        if trade['asset'][k] == 0: continue
        text = f"{k}: {(5-len(k))*' '}{colors.GREEN}{round(trade['asset'][k]/eth, 3)}Ξ{colors.ENDC}"
        text = f"{text}{' '*(28-len(text))}{int(trade['asset'][k]*100/total)}%"
        print_statements.append(text)
    print_statements.append(f"TOTAL: {round(total/eth, 3)}Ξ")
    return print_statements

def print_main_vs_trade(psm, pst):
    left_spacing = max(list(map(lambda x: len(x), psm)))-1
    last = f"{psm[-1]}{(left_spacing-9 - len(psm[-1]))*' '}{'  ≥  ' if (float(psm[-1][6:-1]) >= float(pst[-1][6:-1])) else '  <  '} {pst[-1]}"
    highlight = colors.BLUE if (float(psm[-1][6:-1]) >= float(pst[-1][6:-1])) else colors.RED 
    last = highlight + last + colors.ENDC
    psm = psm[:-1]
    pst = pst[:-1]
    height = max(len(psm), len(pst))

    for i in range(height):
        text = ""
        if i < len(psm):
            text += psm[i] + " "*(left_spacing - len(psm[i]))
            text += "     "
        else:
            text += " "*left_spacing
        if i < len(pst):
            text += pst[i]
        print(text)
    print(last)
    
def print_portfolio(p):
    s = get_portfolio()
    trade = generate_amounts(s, s["wallets"]["trade"])
    prices = generate_prices(s)
    main = generate_amounts(s, s["wallets"]["main"])
    play = generate_amounts(s, s["wallets"]["fun"])
    calculate_position(s, trade, prices)
    calculate_position(s, play, prices)
    calculate_position(s, main, prices)
    pst = print_trade_portfolio(s, trade, play, prices['ethereum'])
    psm = print_main_portfolio(s, main, prices['ethereum'])
    print_main_vs_trade(psm, pst)

    # print_drypowder(p)

# def print_drypowder(p):
#     status_header("dry-powder")
#     usdc_arb = wallet_balance(p["chains"]["arbitrum"], p["wallets"]["main"], "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8", 6)
#     usdc_poly = wallet_balance(p["chains"]["polygon"], p["wallets"]["main"], "0x2791bca1f2de4661ed88a30c99a7a9449aa84174", 6)
#     total = usdc_arb+usdc_poly
#     print(f"Arbitrum USDC: {round(usdc_arb, 2)}")
#     print(f"Polygon USDC: {round(usdc_poly, 2)}")
#     print(colors.BLUE + f"Total USDC: {round(total, 2)}" + colors.ENDC)


def add_token(s, token, coingecko, network, address, decimals, asset=True):
    """
    - s is portfolio.json
    - token: RPL
    - coingecko: rocket-pool
    - network: arbitrum
    - address: 0x...
    - asset if asset, else debt
    """
    token_type = "asset" if asset else "debt"
    token = token.lower()
    if token not in s[token_type].keys():
        s[token_type][token] = {}
    s[token_type][token]["coingecko"] = coingecko
    s[token_type][token][network] = address
    s[token_type][token]["decimals"] = decimals

def print_price(price):
    print(f"Current price: {colors.PURPLE}${round(price, 2)}{colors.ENDC}")

def calculate_position(s, a, p):
    for t in ['asset', 'debt']:
        for k,v in a[t].items():
            a[t][k] = v*p[s[t][k]['coingecko']]

def generate_amounts(s, wallet):
    amounts = {"asset":{"eth":0}, "debt":{}}
    for t in ['asset', 'debt']:
        for k in s[t].keys():
            a = s[t][k]
            amounts[t][k] = 0
            for c in a.keys():
                if c not in s["chains"].keys(): continue
                amounts[t][k] += wallet_balance(s['chains'][c], wallet, a[c], a["decimals"])
    for c in ["optimism", "arbitrum"]:
        amounts["asset"]["eth"] += eth_balance(s["chains"][c], wallet)
    return amounts


def generate_prices(s):
    """returns a dict of prices"""
    prices = set([])
    for k in s['asset']:
        prices.add(s['asset'][k]['coingecko'])
    for k in s['debt']:
        prices.add(s['debt'][k]['coingecko'])
    prices = dict.fromkeys(prices, 0)
    for k in prices:
        prices[k] = coingecko_price(k)
    return prices


def coingecko_price(name):
    res = requests.get(f"https://api.coingecko.com/api/v3/coins/{name}?tickers=false&community_data=false&developer_data=false").json()
    return float(res["market_data"]["current_price"]["usd"])

def wallet_balance(chain, wallet, contract_address, decimal):
    query = f"{chain['api']}api?module=account&action=tokenbalance&contractaddress={contract_address}&address={wallet}&tag=latest&apikey={chain['key']}"
    res = requests.get(query).json()["result"]
    if res == "": return 0
    return int(res)/10**decimal

def eth_balance(chain, wallet):
    query = f"{chain['api']}api?module=account&action=balance&address={wallet}&tag=latest&apikey={chain['key']}"
    res = requests.get(query).json()["result"]
    if res == "": return 0
    return int(res)/10**18



def status_header(title):
    """prints the status"""
    
    print("="*(30-math.floor(len(title)/2)) + " " + colors.BOLD + title.upper() + colors.ENDC + " " + "="*(30-math.ceil(len(title)/2)))

if __name__ == "__main__":
    main()

