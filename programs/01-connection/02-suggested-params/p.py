import json
import pprint

from algosdk.v2client.algod import AlgodClient

ALGOD_ADDRESS = "http://localhost:4001"
ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def getAlgodClient() -> AlgodClient:
    return AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)


client = getAlgodClient()
pprint.pprint(client)

suggested_params = client.suggested_params()

pprint.pprint(suggested_params.first)
pprint.pprint(suggested_params.last)
pprint.pprint(suggested_params.fee)
pprint.pprint(suggested_params.gh)
pprint.pprint(suggested_params.gen)
pprint.pprint(suggested_params.flat_fee)
pprint.pprint(suggested_params.consensus_version)
pprint.pprint(suggested_params.min_fee)
