# Cross wallet money transfer

We have two wallets:
* peter
* ann

Each wallet contains one account:

* wallet peter contains account: home
* wallet ann contains account: work

We populate both accounts peter/home and ann/work with some money from default wallet.

Now we send some money: from peter/home to ann/work

## 1. peter/home account

Create Peter's wallet with home account.

Put some money to this account.

    goal wallet new peter
        -> password: peterpassword

    goal wallet -f peter
    goal account new home

    goal clerk send \
        --amount 100000000000 \
        --from PTRXEOWPFCFJY5J6DCAWBQSZBUXVDLXLPKGRJKXFG66272THGXC2FPI7QE \
        --to home \
        --wallet unencrypted-default-wallet

## 2. ann/work account

Create Ann's wallet with work account.

Put some money to this account.

    goal wallet new ann
        -> password: annpassword

    goal wallet -f ann
    goal account new work

    goal clerk send \
        --amount 100000000000 \
        --from PTRXEOWPFCFJY5J6DCAWBQSZBUXVDLXLPKGRJKXFG66272THGXC2FPI7QE \
        --to work \
        --wallet unencrypted-default-wallet

## 3. CLI: cross wallet money transfer

Send money from Peter's home wallet to Ann's work wallet using CLI:


    goal clerk send \
        --amount 3000000 \
        --from home \
        --to work \
        --wallet peter


## 4. SDK: cross wallet money transfer

Update `p.py`:

    Peter's home account: LLOUQUGAGEHKVO5OOMYDKCDC3TMYH6GVSCSHBL37YUCJAPRBI5C5CLPNXI
    Ann's work account:   6T5A6DIL2XKXFGOKHGEYTLKWKY7IHHBPIAJZN2XIIOWOGVAO7IX3W7SMZ4


Run the code:

    python p.py
