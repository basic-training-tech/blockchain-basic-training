from algosdk import *
from algosdk.v2client.algod import AlgodClient
from algosdk.future import transaction

from utils import validate, print_error, algod_token, algod_server


# DO NOT CHANGE
challenge_id = "3474867148855516251"
client = AlgodClient(algod_token, algod_server)
txids = []

# TODO: Paste your secret key here. You can find it underneath the code editor.
secret_key = ""

# Get the address from the secret key
addr = account.address_from_private_key(secret_key)

# TODO: Get the suggested parameters from the Algod server.
sp = None

# TODO: Create a payment transaction from you to you for 1 Algo
# hint: From and To should be your `addr` and 1 Algo is 1m microAlgos
ptxn = transaction.PaymentTxn(
    sender=None,
    sp=sp,
    receiver=None,
    amt=None
)


# TODO: Sign the transaction.
signed = None

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

except error.AlgodHTTPError as err:
    print_error(str(err))

else:
    print("Verifying the challenge...")
    if validate(challenge_id, txids):
        print("Transactions validated! Collect your badge :)")
    else:
        print(
            "Something went wrong :( Check the error message, update the code and try again!"
        )
