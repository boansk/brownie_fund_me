//SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    mapping(address => uint256) public AddresstoAmountFunded;
    address public owner;
    AggregatorV3Interface public price_feed;
    constructor(address _price_feed_address)  {
        owner = msg.sender;
        price_feed = AggregatorV3Interface(_price_feed_address);
    }

    function fund() public payable {

        uint256 minimumValue = 50;
        require(FundedAmountInUSD(msg.value) >= minimumValue, "Please deposit more than 50 USD");
        AddresstoAmountFunded[msg.sender] += msg.value;
    }

    function withdraw() payable public {
        require(msg.sender == owner);
        payable(msg.sender).transfer(address(this).balance);
    }

    function FundedAmountInUSD(uint256 AmountFunded) public view returns (uint256) {
        uint256 ethPrice = GetPrice();
        uint256 amountFundedinUSD = AmountFunded * ethPrice / 1000000000000000000;
        return amountFundedinUSD / 100000000;
    }

    

    function GetPrice() public  view returns (uint256) {
        (,int256 answer,,,) = price_feed.latestRoundData();
        return uint256(answer);
    }
}