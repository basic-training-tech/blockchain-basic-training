from algosdk.v2client.algod import AlgodClient

ALGOD_ADDRESS = "http://localhost:4001"
ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

client = AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

addr = "PTRXEOWPFCFJY5J6DCAWBQSZBUXVDLXLPKGRJKXFG66272THGXC2FPI7QE"

account_info = client.account_info(addr)
print("Account balance: {} microAlgos".format(account_info.get('amount')))
