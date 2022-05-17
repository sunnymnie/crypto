// SPDX-License-Identifier: MIT

pragma solidity >= 0.6.6 < 0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
//Can import safemath if using solidity < 0.8.0

// Purpose: to accept payment
contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    constructor() public {
        // immediately executed when executed
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minumumUSD = 50 * 10 ** 18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to give me more ETH");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x...);
        return priceFeed.verion()
    }

    function getPrice() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x...);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000); //Need to type-cast

    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 10000000000000000...000000;
        return ethAmountInUsd;

    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _; //rest of the function goes here
    }

    function withdraw() payable onlyOwner public {
        msg.sender.transfer(address(this).balance);
        for (uint256 i=0; i<funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}