from unittest.mock import Mock
from brownie import FundMe, config, network
from scripts.helpful_scripts import get_account, deploy_mockv3aggregator, LOCAL_NETWORKS, FORKED_NETWORKS


def deploy_fund_me():
    print("deploying fund_me contract...")
    account = get_account()
    if network.show_active() not in LOCAL_NETWORKS:
        #use on-chain address
        price_feed_address = config["networks"][network.show_active()]["price_feed_address"]
    else:
        #use mock address
        price_feed_address = deploy_mockv3aggregator()
    fund_me = FundMe.deploy(price_feed_address,{"from": account})
    print(f"fund_me deployed to {fund_me.address}")
    if network.show_active() in FORKED_NETWORKS:
        price = FundMe[-1].GetPrice()
        print(f"price of eth on forked mainnet = {price}")
def main():
    deploy_fund_me()