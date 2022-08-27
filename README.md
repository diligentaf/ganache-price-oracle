# Link
https://www.linkedin.com/pulse/simple-ethereum-oracle-contract-seng-kuang-yap/

# Instruction
```shell
python3 deploy_oracle_contract.py
```

# Terminal 1
```shell
python3 oracle_api.py
```

# Terminal 2 (Price updates every minute)
```shell
python3 client.py
```
Then check contract_address.txt on root directory

# Hardhat
```shell
npx hardhat --network ganache test
npx hardhat help
npx hardhat test
GAS_REPORT=true npx hardhat test
npx hardhat node
npx hardhat run scripts/deploy.ts
```
