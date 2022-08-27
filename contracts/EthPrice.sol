pragma solidity ^0.4.21;

contract PriceOracle {
    // Contract owner
    address public owner;

    // BTC Marketcap Storage
    uint256 public ETHPrice;

    // Callback function
    event CallbackGetETHPrice();

    function updateETHPrice() public {
        // Calls the callback function
        emit CallbackGetETHPrice();
    }

    function setETHPrice(uint256 price) public {
        ETHPrice = price;
    }

    function getETHPrice() public constant returns (uint256) {
        return ETHPrice;
    }

}
