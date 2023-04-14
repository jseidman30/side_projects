# Unit 20 - "Looks like we've made our First Contract!"

---
### Requirements

* public addresses of all you are looking to pay simultaneously
* an ethereum account with enough ETH in it to perform a transaction
* preferably, Metamask
	* you will need to set up a custom, localnet, network in metamask. screenshots can be seen [here](https://github.com/jseidman30/bootcamp-homework/blob/main/20%20-%20Solidity/mm.png)

* preferably, Ganache, to help with network setup and details. also, to see transactions and blocks happening in realtime
* preferably, Remix, to compile the code from scratch if desired. not strictly necessary though

### Instructions

* choose a way to interact with the smart contract. I used Remix
	* contract address: 0x0355BD12676B61cc86fb528A578Cac54cfDc842D

'''''''''''If using Remix'''''''''''''''''''
* copy in/import code from GitHub [full code](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/remix%20smart%20contract%20full%20code.png)
* compile code, ensure no errors
* on deploy and run transactions tab, use injected web3 environment to connect to your Metamask
* input all relevant fields, and select the contract just compiled [deploy and run](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/deploy%20and%20run.png)
* deploy code, input addresses for transfer output. Click transact
* be sure to enter a value large enough to verify transaction success in the "value" field, and then click "deposit" under "deployed contracts" below [deposit and deploy](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/contract%20deployed.png)
* confirm transaction success on Ganache or a block explorer like Etherscan [remix success](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/transaction%20success%20details-remix.png) , [ganache success](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/Ganache%20contract%20run%20result.png) , [ganache results in addresses](https://github.com/jseidman30/bootcamp-homework/blob/main/20-Solidity/Ganache%20transaction%20detail%20screen.png)

''''''''''''''''''''''''''''''''''''''''''''

If accessing the smart contract within other code:
* call the "deposit" function, providing a value of 0 or greater in Gwei
