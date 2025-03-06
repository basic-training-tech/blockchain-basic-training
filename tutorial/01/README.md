# ?


## 1. Working with Algorand's sandbox

Algorand's sandbox is a complete environment that contains
a single blockchain node. It allows you to work with Algorand's
command line tools and API.

To boot the sandbox you need to clone the repo:

    git clone git@github.com:algorand/sandbox.git
    cd sandbox

and run the following command:

    ./sandbox up

The sandbox uses:
* docker
* docker-compose
and you need both of them be installed on your system.

Sandbox is an isolated node which - by default - is not connected to any external network.

Default configuration of the node is:

    ALGOD_ADDRESS = "http://localhost:4001"
    ALGOD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    KMD_ADDRESS = "http://localhost:4002"
    KMD_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

Default wallet:

    ##################################################
    Wallet:	unencrypted-default-wallet (default)
    ID:	d7a02549627e796b2801ea8d4aaed5f1
    ##################################################

Build-in accounts:

    [online]	PTRXEOWPFCFJY5J6DCAWBQSZBUXVDLXLPKGRJKXFG66272THGXC2FPI7QE	PTRXEOWPFCFJY5J6DCAWBQSZBUXVDLXLPKGRJKXFG66272THGXC2FPI7QE	4000004000000000 microAlgos
    [offline]	SBAR6AROAPJCDL7TCY2WOUZJRYHLMJFHXXVVAYDI4QTNWFB6OLBOBSFU7M	SBAR6AROAPJCDL7TCY2WOUZJRYHLMJFHXXVVAYDI4QTNWFB6OLBOBSFU7M	4000004000000000 microAlgos
    [offline]	ZJDUSUDA7FIGOCVGULGHIR67GFSKRDVYKYM5LPTLRCQDRRE2XWRCWJVULE	ZJDUSUDA7FIGOCVGULGHIR67GFSKRDVYKYM5LPTLRCQDRRE2XWRCWJVULE	1000001000000000 microAlgos

Special accounts:

    Fee sink:      A7NMWS3NT3IUDMLVO26ULGXGIIOUQ3ND2TXSER6EBGRZNOBOUIQXHIBGDE
    Rewards Pool:  7777777777777777777777777777777777777777777777777774MSJUVU

If you want to bring the sandbox down you can just remove the containers:

    docker rm -f $(docker ps -a -q)

Once you have the images prepared (this is done during the first up command) then
the complete procedure to boot sandbox take just a couple of seconds.

Keep in mind that if you delete the containers and start the sandbox again
you will get a pristine new environment with default wallet and default account
but without any transactions or accounts that you may have created during
previous runs of the environment.

## 2. goal cli command

The sandbox contains `algorand-sandbox-algod` docker container which allows you to run
`goal` cli command.

Start the sandbox and then run the command:

        docker exec -it algorand-sandbox-algod /bin/bash

It will open ssh session to Algorand's container.
Now you can run `goal` commands:

        goal version
        goal help

Once you are done you can close the ssh session with `exit` command.


## 3. Info about the node

The following commands print various information about the node and the network:

    goal report
    goal node status
    goal network status --rootdir /opt/testnetwork

You can also check the amount of money available in the ledger:

    goal ledger supply

## 3. Default wallet and accounts






docker exec -it algorand-sandbox-algod /bin/bash





        goal wallet list
        goal wallet new ABCDEF

        goal account list
        goal account list --info
        goal account new LOREM

        goal node status
        goal version
