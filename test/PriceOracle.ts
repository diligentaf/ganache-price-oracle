import { ethers } from "hardhat";
import { Contract, ContractFactory, constants, BigNumber } from "ethers";
import path from "path";
import fs from "fs";

describe("Price Oracle Testing", function () {
  const aggregatorAddress = fs.readFileSync(
    path.join(__dirname, "../contract_address.txt"),
    "utf-8"
  );

  let addr0, addr1, addr2, addr3, addrs;
  let EthPrice: Contract;

  before(async function () {
    const [_addr0, _addr1, _addr2, _addr3, ..._addrs] =
      await ethers.getSigners();
    addr0 = _addr0;
    addr1 = _addr1;
    addr2 = _addr2;
    addr2 = _addr2;
    addr3 = _addr3;
    addrs = _addrs;

    // const PriceOracleFactory = await ethers.getContractFactory("OraclePrice");
    // PriceOracle = await PriceOracleFactory.connect(addr0).deploy(
    //   aggregatorAddress
    // );
    EthPrice = await ethers.getContractAt("PriceOracle", aggregatorAddress);
  });

  describe("fetch oracle data", function () {
    it("consoling the token address", async function () {
      let bint = BigInt(await EthPrice.getETHPrice())
      console.log(Number(bint * 100n / 100n) / 100);
    });
  });
});
