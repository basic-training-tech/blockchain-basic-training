# Sandbox

## 1. Up / Down

Up:

    git clone git@github.com:algorand/sandbox.git
    cd sandbox
    ./sandbox up

Down:

    docker rm -f $(docker ps -a -q)

## 2. Info

Sandbox is an isolated node which - by default - is not connected to any test network.

Default config:

    ALGOD_ADDRESS = "http://localhost:4001"
    ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    KMD_ADDRESS = "http://localhost:4002"
    KMD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

Default wallet (the wallet ID changes everytime you build the container):

    # listed with
    # goal wallet list

    ##################################################
    Wallet:	unencrypted-default-wallet (default)
    ID:	922027ee41ffd822701e027f38eb6bde
    ##################################################

Build-in accounts (build-in accounts change  everytime you build the container):

    # listed with
    # goal account list

    [offline]	F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM	F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM	4000000000000000 microAlgos
    [offline]	TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4	TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4	1000000000000000 microAlgos
    [online]	Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA	Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA	4000000000000000 microAlgos


Technical accounts:

    # listed with
    # web interface: https://explorer.dappflow.org

    Fee Sink [NotParticipating]:        A7NMWS3NT3IUDMLVO26ULGXGIIOUQ3ND2TXSER6EBGRZNOBOUIQXHIBGDE
    RewardsPool [NotParticipating]:     7777777777777777777777777777777777777777777777777774MSJUVU


Unknown account (???):

    # listed with
    # web interface: https://explorer.dappflow.org

    QAHHJNC2MF3E6DDV6HJAC53DLT46WGJ7C6MEZFYCUN66SOONJJEHHMFROM [online]
        Balance         1,000,001,000
        Minimum balance 0.1


Ports:

    4001 - algod
    4002 - kmd
    9392 - cdt (debugger)
    8980 - indexer

The token inside docker container:

    # algod token
    docker exec -it algorand-sandbox-algod /bin/bash
    cat /opt/testnetwork/Node/algod.token


    # kmd token
    docker exec -it algorand-sandbox-algod /bin/bash
    cat /opt/testnetwork/Node/kmd-v0.5/kmd.token

The wallets inside docker container:

    docker exec -it algorand-sandbox-algod /bin/bash
    ls -la /opt/testnetwork/Node/kmd-v0.5/sqlite_wallets

## 3. External commands

    ./sandbox goal node status

    ./sandbox goal wallet list
    ./sandbox goal wallet new

    ./sandbox goal account new
    ./sandbox goal account list

    ./sandbox goal clerk send

    ./sandbox test

## 4. Running goal commands inside the container

    docker exec -it algorand-sandbox-algod /bin/bash

    goal wallet list
    goal wallet new ABCDEF

    goal account list
    goal account list --info
    goal account new LOREM

    goal node status
    goal version

## 5. Changing the token

### 5.1. Solution #1: rebuild containers

If you want to use different token:
* update `docker-compose.yml` file in sandbox
* change token in two places
* rebuild images

Rebuilding image updates:
* default wallet
* default accounts

### 5.2. Solution #2: regenerate token inside container

Stop the node and then regenerate token:

    goal node stop
    goal node generatetoken
    goal node start

    cat /opt/testnetwork/Node/algod.token

    goal kmd stop
    cat /opt/testnetwork/Node/algod.token > /opt/testnetwork/Node/kmd-v0.5/kmd.token
    goal kmd start

## 6. API & httpie

* https://developer.algorand.org/docs/rest-apis/restendpoints/

API documentation:
* https://developer.algorand.org/docs/rest-apis/algod/v2/

Algod (4001):

    http http://localhost:4001/health
    http http://localhost:4001/genesis
    http http://localhost:4001/metrics
    http http://localhost:4001/swagger.json
    http http://localhost:4001/versions

    http "http://localhost:4001/v2/status?pretty" X-Algo-API-Token:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    http http://localhost:4001/v2/accounts/Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA X-Algo-API-Token:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    http http://localhost:4001/v2/accounts/Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA X-Algo-API-Token:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    http http://localhost:4001/v2/ledger/supply X-Algo-API-Token:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


KMD (4002):

    http http://localhost:4002/v1/wallets X-KMD-API-Token:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    http http://localhost:4002/versions
    http http://localhost:4002/swagger.json



Indexer (8980):

    http http://localhost:8980/health

    http http://localhost:8980/v2/accounts
    http http://localhost:8980/v2/assets
    http http://localhost:8980/v2/transactions
    http http://localhost:8980/v2/applications

    http "http://localhost:8980/v2/transactions?pretty"

    http http://localhost:8980/v2/blocks/10
    http http://localhost:8980/v2/transactions?txid=123


## 7. Web interface

    https://explorer.dappflow.org

## 8. Info about the node

The following commands print various information about the node and the network:

    docker exec -it algorand-sandbox-algod /bin/bash
    goal report
    goal node status
    goal network status --rootdir /opt/testnetwork


You can also check the amount of money available in the ledger:

    goal ledger supply
