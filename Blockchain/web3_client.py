import json
import os
from web3 import Web3

# Connect to local blockchain (Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

assert w3.is_connected(), "Blockchain not connected"

# Contract details
contract_address = "YOUR_CONTRACT_ADDRESS_HERE"

with open("FraudStorageABI.json", "r") as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(
    address=contract_address,
    abi=contract_abi
)

private_key = os.getenv("PRIVATE_KEY")
account = w3.eth.accounts[0]


def store_on_blockchain(data_hash: str, is_fraud: bool):
    """
    Stores hash and prediction on blockchain
    """

    nonce = w3.eth.get_transaction_count(account)

    tx = contract.functions.storeRecord(
        data_hash,
        is_fraud
    ).build_transaction({
        "from": account,
        "nonce": nonce,
        "gas": 2_000_000,
        "gasPrice": w3.to_wei("20", "gwei")
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("Transaction sent")
    print("Tx hash:", tx_hash.hex())

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction confirmed")
    print("Block number:", receipt.blockNumber)

    return tx_hash.hex()
