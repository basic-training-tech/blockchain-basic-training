# napster training 2

## Info

https://developer.algorand.org/docs/get-started/dapps/

video: https://drive.google.com/file/d/1jjvFIa_qtCaudvH7QpBVlRUjdvN6nN85/view?userstoinvite=none

Discussions:

    discord.gg/algorand

demo-abi repo:

    https://github.com/algorand-devrel/demo-abi

we need python 3.10

    pyenv
    pyenv versions

    pip install pyteal
    pip install -r requirements.txt

WASABI:

    https://github.com/fionnachan/wasabi

Explorer:

    https://explorer.dappflow.org


## FULL RUN

    # in sandbox
    ./sandbox up

    # in demo-abi
    ./manage.sh create

    # verify transactions with
    curl "localhost:8980/v2/transactions?pretty" | jq
    curl "localhost:8980/v2/accounts?pretty" | jq
    curl "localhost:8980/v2/assets?pretty" | jq

    # in https://algo-wasabi.netlify.app/
    - update self-defined app use
    - paste contract json
    - use api

    # in https://explorer.dappflow.org
    - configure access with sandbox
    - view transactions / accounts / applications


To view transaction executed in DEMO-ABI:
* visit https://explorer.dappflow.org/
* go to applications
* select link in CREATOR column
* you will see a list of transactions

How to list application transactions with goal CLI?

    goal app info --app-id=15
    goal account info -a F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM
