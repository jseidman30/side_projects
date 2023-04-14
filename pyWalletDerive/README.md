# Multi-Blockchain Wallet in Python

 ### description

  - this wallet can create new full instances (public address, public key, private key, publickeyhash) of BTC, BTC testnet, or Ethereum wallets inline, convert private keys to usable python variables, create and send transactions using the previously generated info, and estimate gas requirements/usage
  
  #### required downloads
  
  * bit (using pip)
  * web3 (using pip)
  * [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive)
  
  #### dependencies
  
  * subprocess
  * json
  * load_dotenv from dotenv
  * os
  * ticker value constants, manually created in a .py file. screenshot can be found [here](https://github.com/jseidman30/bootcamp-homework/blob/main/19-Blockchain%20Python/screenshots/Screen%20Shot%202021-08-31%20at%2012.15.56%20AM.png)
  * PrivateKeyTestnet and NetworkAPI, from bit and bit.network, respectively
  * Web3 and geth_poa_middleware, from web3 and web3.middleware, respectively
  * Account from eth_account
  
  #### usage instructions

  * it will be necessary to clone the repo for hd-wallet-derive and move it to the working directory, so do that
  
  * make sure the addressFrom has enough balance to send
  
  * load your mnemonic phrase file, stumble your way through the functions, and off you go
      ** see screenshots [screenshots](https://github.com/jseidman30/bootcamp-homework/tree/main/19-Blockchain%20Python/screenshots) for additional details
