from brownie import FundMe, MockV3Aggregator

def show_fund_me_contracts():
    print(f"FundMe contract lenth = {len(FundMe)}")

def show_mock_contracts():
    print(f"Mock contract length = {len(MockV3Aggregator)}")

def main():
    show_fund_me_contracts()
    show_mock_contracts()