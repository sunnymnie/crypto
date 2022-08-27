import requests
import json
import os
from enum import Enum, auto
import math


class bcolors:
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


def print_portfolio(p):
    #  print_asset("ethereum", Asset.ETH, ethereum_bitcoin_additional)
    #  print_asset("rocket-pool", Asset.RPL)
    #  print_asset("magic", Asset.MAGIC)
    #  print_battlefly()
    print_drypowder(p)

def print_drypowder(p):
    status_header("dry-powder")
    usdc_arb = wallet_balance(p["chains"]["arbitrum"], p["wallets"]["main"], "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8", 6)
    usdc_poly = wallet_balance(p["chains"]["polygon"], p["wallets"]["main"], "0x2791bca1f2de4661ed88a30c99a7a9449aa84174", 6)
    total = usdc_arb+usdc_poly
    print(f"Arbitrum USDC: {round(usdc_arb, 2)}")
    print(f"Polygon USDC: {round(usdc_poly, 2)}")
    print(bcolors.BLUE + f"Total USDC: {round(total, 2)}" + bcolors.ENDC)


def conditional_buy(asset, h24, d7):
    buy_24h = asset[0](h24)
    buy_7d = asset[1](d7)
    print(f"24h change: {bcolors.GREEN if h24 > 0 else bcolors.RED}{round(h24, 2)}%{bcolors.ENDC}          buy ${buy_24h}")
    print(f"7d  change: {bcolors.GREEN if d7 > 0 else bcolors.RED}{round(d7, 2)}%{bcolors.ENDC}          buy ${buy_7d}")
    if buy_24h+buy_7d >= MIN_BUY:
        print(f"{bcolors.BLUE}Total buy amount: ${buy_24h+buy_7d}{bcolors.ENDC}")
    else:
        print("Total buy amount: $0")
    return buy_24h+buy_7d if buy_24h+buy_7d >= MIN_BUY else 0

def print_price(price):
    print(f"Current price: {bcolors.PURPLE}${round(price, 2)}{bcolors.ENDC}")

#  def ethereum_bitcoin_additional(eth, eth_24, eth_7d):
#      btc, btc_24, btc_7d = coingecko_price("bitcoin")
#      print(f"ETH/BTC 24h change: {round(eth_24-btc_24, 2)}%        7d change: {round(eth_7d-btc_7d, 2)}%")
#      if btc_24-eth_24>0 and btc_7d-eth_7d>0:
#          print(bcolors.BLUE + "Go long ETH and short BTC on Aave" + bcolors.ENDC)

def print_asset(name, asset, additional=None):
    status_header(name)
    p, p24, p7d = coingecko_price(name)
    print_price(p)
    #  amt = conditional_buy(asset, p24, p7d)
    #  if additional: additional(p, p24, p7d)
    #  return amt


def print_battlefly():
    status_header("battlefly")
    res = requests.get("https://hfihu314z3.execute-api.us-east-1.amazonaws.com/collection/arb/0x0af85a5624d24e2c6e7af3c0a0b102a28e36cea3").json()
    floor = int(res["floorPrice"])/1000000000000000000
    magic, magic_24h, magic_7d = coingecko_price("magic")
    magic_position = wallet_balance(Chain.ARB, WALLET_FUN, "0x539bdE0d7Dbd336b79148AA742883198BBF60342", 18)
    print(f"Current floor: {bcolors.PURPLE}{round(floor, 2)} MAGIC{bcolors.ENDC}     or      {bcolors.PURPLE}${round(magic*floor, 2)}{bcolors.ENDC}")
    nft_position = floor*BATTLEFLY_NFTS
    portfolio_position = nft_position/(nft_position+magic_position)
    print(f"Position: {bcolors.PURPLE}{round(100*portfolio_position, 2)}%{bcolors.ENDC} BattleFly NFTs")
    if portfolio_position > 0.9:
        print(bcolors.YELLOW + "Portfolio is too Battlefly weighted > 90%. Buy more MAGIC"+bcolors.ENDC)
    elif portfolio_position < 0.75:
        print(bcolors.YELLOW + f"Portfolio needs to buy more BattleFlies (currently {BATTLEFLY_NFTS})" + bcolors.ENDC)


def coingecko_price(name):
    res = requests.get(f"https://api.coingecko.com/api/v3/coins/{name}?tickers=false&community_data=false&developer_data=false").json()
    return float(res["market_data"]["current_price"]["usd"]), float(res["market_data"]["price_change_percentage_24h"]), float(res["market_data"]["price_change_percentage_7d"])

def wallet_balance(chain, wallet, contract_address, decimal):
    query = f"{chain['api']}api?module=account&action=tokenbalance&contractaddress={contract_address}&address={wallet}&tag=latest&apikey={chain['key']}"
    res = requests.get(query).json()["result"]
    return int(res)/10**decimal



def status_header(title):
    """prints the status"""
    
    print("="*(30-math.floor(len(title)/2)) + " " + bcolors.BOLD + title.upper() + bcolors.ENDC + " " + "="*(30-math.ceil(len(title)/2)))

if __name__ == "__main__":
    main()

