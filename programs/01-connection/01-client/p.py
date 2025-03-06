import pprint

from algosdk.v2client.algod import AlgodClient

ALGOD_ADDRESS = "http://localhost:4001"
ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def getAlgodClient() -> AlgodClient:
    return AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)


client = getAlgodClient()
pprint.pprint(client)

# documentation: https://py-algorand-sdk.readthedocs.io/en/latest/algosdk/v2client/algod.html#

print("\n\n=====> status")
pprint.pprint(client.status())

print("\n\n=====> health")
pprint.pprint(client.health())

print("\n\n=====> versions")
pprint.pprint(client.versions())

print("\n\n=====> genesis")
pprint.pprint(client.genesis())
# pprint.pprint(client.account_info(ALGOD_ADDRESS))
