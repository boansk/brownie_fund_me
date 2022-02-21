from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

MOCK_DECIMAL = 8
MOCK_ANSWER = Web3.toWei(2000, "ether")
LOCAL_NETWORKS = ["development", "ganache-local"]
FORKED_NETWORKS = ["mainnet-fork"]

def get_account():
    if network.show_active() in LOCAL_NETWORKS or network.show_active() in FORKED_NETWORKS:
        account = accounts[0]
        print(f"account[0] = {account}")
        return account
    else:
        account = accounts.add(config["wallet"]["from_key"])
        print(f"account = {account}")
        return account


def deploy_mockv3aggregator():
    if len(MockV3Aggregator) <=0:
        print("deploying mock...")
        MockV3Aggregator.deploy(MOCK_DECIMAL, MOCK_ANSWER, {"from": get_account()})
    
    price_feed_address = MockV3Aggregator[-1]
    print(f"mock deployed at {price_feed_address}")
    return price_feed_address