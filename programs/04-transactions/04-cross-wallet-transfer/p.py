import pprint

from algosdk.kmd import KMDClient
from algosdk.v2client.algod import AlgodClient
from algosdk.future import transaction

txids = []
ALGOD_ADDRESS = "http://localhost:4001"
ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

client = AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)
sp = client.suggested_params()

# sender: peter/home
senders_address = "LLOUQUGAGEHKVO5OOMYDKCDC3TMYH6GVSCSHBL37YUCJAPRBI5C5CLPNXI"
account_info_a = client.account_info(senders_address)
print("A balance: {} microAlgos".format(account_info_a.get('amount')))



# receiver: ann/work
receivers_address = "6T5A6DIL2XKXFGOKHGEYTLKWKY7IHHBPIAJZN2XIIOWOGVAO7IX3W7SMZ4"
account_info_b = client.account_info(receivers_address)
print("B balance: {} microAlgos".format(account_info_b.get('amount')))



# TODO: Create a payment transaction from you to you for 1 Algo
# hint: From and To should be your `addr` and 1 Algo is 1m microAlgos
ptxn = transaction.PaymentTxn(
    sender=senders_address,
    sp=sp,
    receiver=receivers_address,
    amt=1000000
)

KMD_ADDRESS = "http://localhost:4002"
KMD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def getKmdClient() -> KMDClient:
    return KMDClient(KMD_TOKEN, KMD_ADDRESS)

kmd = getKmdClient()

KMD_WALLET_NAME = "peter"
KMD_WALLET_PASSWORD = "peterpassword"

wallets = kmd.list_wallets()
walletID = None
for wallet in wallets:
    pprint.pprint("-----------> wallet " + wallet["name"])
    if wallet["name"] == KMD_WALLET_NAME:
        walletID = wallet["id"]
        break

if walletID is None:
    raise Exception("Wallet not found: {}".format(KMD_WALLET_NAME))

walletHandle = kmd.init_wallet_handle(walletID, KMD_WALLET_PASSWORD)


secret_key_a = kmd.export_key(walletHandle, KMD_WALLET_PASSWORD, senders_address)



# # TODO: Sign the transaction.
signed = ptxn.sign(secret_key_a)

# Send the transaction, returns the transaction id for
# the first transaction in the group

try:
    # Send the transaction to the network
    # this returns the first transaction id in the group
    txId = client.send_transaction(signed)

    # Add txid to list to be validated later
    txids.append(txId)

    # Wait for the transaction to be confirmed.
    result = transaction.wait_for_confirmation(client, txId, 2)

    # Log out the confirmed round
    print(f"Confirmed round: {result['confirmed-round']}")

except:
    print("ERR.....")

else:
    print("Done...")
    # if validate(challenge_id, txids):
    #     print("Transactions validated! Collect your badge :)")
    # else:
    #     print(
    #         "Something went wrong :( Check the error message, update the code and try again!"
    #     )

account_info_a = client.account_info(senders_address)
print("A balance: {} microAlgos".format(account_info_a.get('amount')))

account_info_b = client.account_info(receivers_address)
print("B balance: {} microAlgos".format(account_info_b.get('amount')))
