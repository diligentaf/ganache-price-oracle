// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./libs/AggregatorInterface.sol";

contract OraclePrice {
  AggregatorInterface internal ref;
  // For ETH-USD on ropsten, input the address:
  // 0x8468b2bDCE073A157E560AA4D9CcF6dB1DB98507

  constructor(address _aggregator) public {
    ref = AggregatorInterface(_aggregator);
  }

  function getLatestAnswer() public view returns (int256) {
    return ref.latestAnswer();
  }
}