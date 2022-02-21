from webbrowser import get
from brownie import accounts, FundMe, MockV3Aggregator, network
from scripts.helpful_scripts import get_account, LOCAL_NETWORKS, FORKED_NETWORKS

def get_price():
    if network.show_active() in LOCAL_NETWORKS:
        print("getting mock contract data....")
        mock_aggregator = MockV3Aggregator[-1]
        roundId,answer,startedAt,updatedAt,answeredInRound = mock_aggregator.latestRoundData()
        print(f"mock price = {answer}")
    else:
        print(f"getting price from network...")
        price = FundMe[-1].GetPrice()
        print(f"price of eth = {price}")
        
def fund():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.fund({"from":account, "value": 30000000000000000})

def main():
    get_price()