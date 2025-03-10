import pprint

from algosdk.v2client.algod import AlgodClient
from algosdk.kmd import KMDClient
from account import Account

ALGOD_ADDRESS = "http://localhost:4001"
ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def getAlgodClient() -> AlgodClient:
    return AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

client = AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)


KMD_ADDRESS = "http://localhost:4002"
KMD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def getKmdClient() -> KMDClient:
    return KMDClient(KMD_TOKEN, KMD_ADDRESS)


# KMD_WALLET_NAME = "unencrypted-default-wallet"
# KMD_WALLET_PASSWORD = ""


#
# Create a new wallet with:
#         docker exec -it algorand-sandbox-algod /bin/bash
#         goal wallet new ABCDEF
#
# Set default wallet with:
#         goal wallet -f ABCDEF
#
#
# Crate account:
#         goal account new LOREM
#
#
KMD_WALLET_NAME = "euro"
KMD_WALLET_PASSWORD = "loremipsum"


# Create a new wallet with:
#         docker exec -it algorand-sandbox-algod /bin/bash
#         goal wallet new some-wallet
#
# KMD_WALLET_NAME = "some-wallet"
# KMD_WALLET_PASSWORD = ""


kmd = getKmdClient()

wallets = kmd.list_wallets()
walletID = None
for wallet in wallets:
    pprint.pprint("-----------> wallet " + wallet["name"])
    if wallet["name"] == KMD_WALLET_NAME:
        walletID = wallet["id"]
        break

if walletID is None:
    raise Exception("Wallet not found: {}".format(KMD_WALLET_NAME))


pprint.pprint("==wallet=================================")
pprint.pprint(wallet)
pprint.pprint(wallet["name"])
pprint.pprint(walletID)

walletHandle = kmd.init_wallet_handle(walletID, KMD_WALLET_PASSWORD)

pprint.pprint("-----> handle acquired")
try:
    addresses = kmd.list_keys(walletHandle)
    privateKeys = [
        kmd.export_key(walletHandle, KMD_WALLET_PASSWORD, addr)
        for addr in addresses
    ]
    kmdAccounts = [Account(sk) for sk in privateKeys]
finally:
    kmd.release_wallet_handle(walletHandle)


pprint.pprint("==privateKeys=================================")
pprint.pprint(privateKeys)

pprint.pprint("==kmdAccounts=================================")
pprint.pprint(kmdAccounts)
for ac in kmdAccounts:
    pprint.pprint("---account------------------------------------------------------")
    pprint.pprint("---account------------------------------------------------------")
    pprint.pprint(ac.getAddress())
    pprint.pprint(ac.sk)
    pprint.pprint(ac.getMnemonic())
    pprint.pprint(ac.getPrivateKey())
    account_info = client.account_info(ac.getAddress())
    pprint.pprint(account_info)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))
