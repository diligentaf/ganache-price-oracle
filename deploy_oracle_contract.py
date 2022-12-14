import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from solcx import compile_files,get_solc_version,get_installed_solc_versions, set_solc_version,compile_source,install_solc
import json
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
if w3.isConnected():
    if web3.__version__.split(".")[0] == "4":
        w3.middleware_stack.inject(geth_poa_middleware,layer=0)
    else:
        w3.middleware_onion.inject(geth_poa_middleware,layer=0)
else:
    assert False, "No connection"
w3.eth.defaultAccount = w3.eth.accounts[0]

install_solc('v0.4.25')
print("installed solc version:",get_installed_solc_versions())
set_solc_version('v0.4.25')
contract = '''
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
'''
compiled = compile_source(contract)
contract = w3.eth.contract(abi=compiled['<stdin>:PriceOracle']['abi'],bytecode=compiled['<stdin>:PriceOracle']['bin'])
tx_hash = contract.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
with open("abi.txt","w") as f:
    json.dump(compiled['<stdin>:PriceOracle']['abi'],f)
with open("bytecode.txt","w") as f:
    f.write(compiled['<stdin>:PriceOracle']['bin'])
with open("contract_address.txt","w") as f:
    f.write(tx_receipt.contractAddress)
