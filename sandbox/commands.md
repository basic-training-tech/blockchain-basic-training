# Tasks

    docker exec -it algorand-sandbox-algod /bin/bash

## 1. Default wallet, default accounts, money transfer

    goal wallet list

    goal account list
    goal account list --info

    goal clerk send \
        --amount 8000000000000 \
        --from Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA \
        --to TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4

    goal clerk send \
        --amount 8000000000000 \
        --from TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4 \
        --to F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM

    goal clerk send \
        --amount 8000000000000 \
        --from F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM \
        --to Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA


## 2. Default wallet, new accounts, money transfer

    goal wallet list

    goal account list
    goal account list --info

    goal account new JOHN
    goal account list


Send to JOHN:

    # 90 Algo === 90 mln
    goal clerk send \
        --amount 90000000 \
        --from Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA \
        --to JOHN

    goal clerk send \
        --amount 90000000 \
        --from TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4 \
        --to JOHN

    goal clerk send \
        --amount 90000000 \
        --from F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM \
        --to JOHN


Send from JOHN:

    # 5 algo === 5 mln
    goal clerk send \
        --amount 5000000 \
        --from JOHN \
        --to Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA

    goal clerk send \
        --amount 5000000 \
        --from JOHN \
        --to TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4

    goal clerk send \
        --amount 5000000 \
        --from JOHN \
        --to F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM


## 3. New wallet, new accounts, money transfer

    goal wallet list

    goal wallet new euro
    goal wallet -f euro
    goal wallet list

    goal account list

    goal account new PETER
    goal account list


Send to PETER (default wallet does not matter):

    goal clerk send \
        --amount 90000000 \
        --from Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA \
        --to PETER \
        --wallet unencrypted-default-wallet


## 4. Delete an account

    # PETER
    goal account delete -a LOGVNAKIMIBYL7UCGAAKQANZMM3VOMNJK6RPJCLMFYJRAWROPXXW3KGY5U

Now the command:

    goal account list

returns empty list.

But the account is still visible at: https://explorer.dappflow.org/explorer/accounts


## 5. Create an asset

    goal wallet -f unencrypted-default-wallet
    goal asset create --name foobar --creator Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA --total 10000
    goal asset create --name abcdef --creator Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA --total 1000


List assets and apps of an account:

    goal account info -a Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA

Info about asset:

    goal asset info --assetid=11
    goal asset info --assetid=12

## 6. Send an asset to another account

We want to send asset to:

    TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4


First: self transfer of an asset: 0 units

    # ok: amount 0
    # --from and --to: the account that wants to accept the asset
    goal asset send \
        --assetid 11 \
        --amount 0 \
        --to TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4 \
        --from TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4

    goal account info -a TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4

Then: send the asset from creator to the new account:

    goal asset send \
        --assetid 11 \
        --amount 10 \
        --to TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4 \
        --from Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA


    goal asset info --assetid=11

    goal account info -a TS5PCOLCF2OXD3W3LIPACPLJIAJZOMKFZ2XKTOTJSDM5VLBFTKSAZ5WWG4
    goal account info -a Y3I4T4UNGVEQ6EM6RPTKVVNZEV425B2H72URAJLYK7523XHJWMSO4VAXZA


## 6. Delete a wallet

Is this procedure correct?


Delete account in the wallet:

    goal account delete -a X

Delete wallet:

    goal wallet list
    cd /opt/testnetwork/Node/kmd-v0.5/sqlite_wallets
    ls -la
    goal kmd stop
    rm unencrypted-default-wallet.d7a02549627e796b2801ea8d4aaed5f1.db
    goal kmd start
    goal wallet list
