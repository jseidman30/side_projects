# eCoin network startup instructions

## Program(s) required

* Mostly just Geth (currently working on 1.9.7) + tools.

* You will also need an ethereum or EVM compatible address (at least one)

**We used MyCrypto to create a new ethereum/EVM address and account**

---

## Node setup

### this section assumes the network has already been created, and you are trying to launch a node on the network

#### if you are looking to create your own version of a testnet network, please refer to [POA Blockchain guide](https://github.com/jseidman30/bootcamp-homework/blob/main/18-Blockchain/POA-Blockchain-guide.md) 

* from your Geth folder, call the function to initialize the node on the network using the network's JSON file and the Geth executable
	** example: "./geth --datadir YOURNODENAMEHERE init YOURNETWORKNAMEHERE.json"

---

## Node validating transactions/mining

* from your Geth folder, call the function to unlock the node by address, begin mining, specify the port to access, and allow for riskier settings (because we are on testnet), respectively, in the code below

	** example: ./geth --datadir YOURNODENAMEHERE --unlock YOURNODEPUBLICADDRESSHERE --mine --port PORTSPECIFIEDBYINTEGER --bootnodes "enode://ENODEINFOFROMCHAINORIGIN@IPADDRESSOFNODE:PORTNUMBER --ipcdisable --allow-insecure-unlock

**additional details, examples, and screenshots are available in [eCoin github](https://github.com/jseidman30/bootcamp-homework/tree/main/18-Blockchain)**

---

### network details

* block time: appx 30 seconds per block
* existing nodes' passwords: names of each of the nodes

---

## Connecting eCoin to MyCrypto

* open the MyCrypto app and access your keystore file generated during the initialization of the node
	** the keystore file will be located in the file with your node's name, which most likely is in your Geth folder

* enter node/keystore password. See above section for existing nodes' passwords

* click "change network" at the bottom of the menu on the left side of MyCrypto

* scroll all the way down to "+ add custom node"

* on the new popout window, change the network before doing anything else. Again, scroll all the way to the bottom to "Custom"
	** once "Custom" is selected, additional fields will be present

* Node name: YOURNODENAME
* Network: Custom
* My Network name: eCoin
* Currency: ECOIN
* Chain ID: 666
* URL: currently using localhost ("https://127.0.0.1:8545")

* screenshots of the setup process are available and located in [eCoin github](https://github.com/jseidman30/bootcamp-homework/tree/main/18-Blockchain)





