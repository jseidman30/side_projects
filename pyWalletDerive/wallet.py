# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os
from constants import *
from bit import *
from web3 import *
from web3.middleware import geth_poa_middleware

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("BIP39_MNEMONIC")

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Create a function called `derive_wallets`
def derive_wallets(coin,mnemonic):
    command = "php '/Users/jeremyseidman/Desktop/geth-alltools-darwin-amd64-1.9.7-a718daa6/hd-wallet-derive' -g --mnemonic --cols=all --coin=coin --numderive=1 --format=json"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
    ["BTC"=derive_wallets(BTC,mnemonic)],
    ["BTCTEST"=derive_wallets(BTCTEST,mnemonic)],
    ["ETH"=derive_wallets(ETH,mnemonic)]
}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,rawkey):
    acctinfo = Account.from_key(os.getenv("'"&rawkey&"'"))
    return acctinfo

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(acct, recipient, amt):
    gasest = w3.eth.estimateGas(
        {"from": acct.address, "to": recipient, "value": amt}
    )
    return {
        "chainId": 666, 
        "from": acct.address,
        "to": recipient,
        "value": amt,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasest,
        "nonce": w3.eth.getTransactionCount(acct.address),
    }


# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(acct, recipient, amt):
    tx = create_tx(acct, recipient, amt)
    signed_tx = acct.sign_transaction(tx)
    output = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(output.hex())
    return output.hex()
