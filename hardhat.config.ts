import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {
  solidity: {
    compilers: [
      {
        version: "0.6.0",
      },
      {
        version: "0.6.7",
      },
      {
        version: "0.4.21",
      },
      // {
      //   version: "0.8.7",
      //   settings: {
      //     optimizer: {
      //       enabled: true,
      //       runs: 200,
      //     },
      //   },
      // },
    ],
  },
  networks: {
    ganache: {
      url: "http://127.0.0.1:8545",
    },
  },
};

export default config;
