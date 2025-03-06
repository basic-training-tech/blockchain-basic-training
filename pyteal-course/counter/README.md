# pyteal course: counter

* https://www.youtube.com/watch?v=V3d3VTlgMo8&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=1
* https://www.youtube.com/watch?v=a25ol9NPBTM&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=2
* https://www.youtube.com/watch?v=h2DkDyViZb0&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=3
* https://www.youtube.com/watch?v=w1eYtAR5brY&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=4
* https://www.youtube.com/watch?v=o2L3MD-zKQ8&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=5
* https://www.youtube.com/watch?v=Uv23g3uNHWE&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=6
* https://www.youtube.com/watch?v=sR6WjM4cpPU&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=7

## VIDEO 1

Code:

* https://github.com/algorand-devrel/pyteal-course


Sandbox volume:

    volumes:
      - type: bind
        source: ../pyteal-course
        target: /data



## VIDEO 2

The code:

    # contracts/my/step_01.py
    from pyteal import *

    def approval():
        return Approve()

    def clear():
        return Approve()



The commands:

    pip install -r ./requirements.txt
    ./build.sh contracts.my.step_01

The result: files in `build/` folder.

## VIDEO 3

    from pyteal_helpers import program

    def approval():
        global_owner = Bytes("owner") # byteslice
        global_counter = Bytes("counter") # int
        return program.event(
            init=Seq(
                App.globalPut(global_counter, Int(0)),
                App.globalPut(global_owner, Txn.sender()),
                Approve(),
            ),
            #no_op=,
        )


Compile:

    ./build.sh contracts.my.step_02


## VIDEO 4


    ./sandbox enter algod


    ONE=F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM

    goal app create \
        --creator $ONE \
        --approval-prog /data/build/approval.teal \
        --clear-prog /data/build/clear.teal \
        --global-byteslices 1 \
        --global-ints 1 \
        --local-byteslices 0 \
        --local-ints 0


    goal app info --app-id 1

    goal app read --global --app-id 1
    goal app read --global --app-id 1 --guess-format


## VIDEO 5

Code:

    from pyteal import *
    from pyteal_helpers import program

    def approval():
        global_owner = Bytes("owner") # byteslice
        global_counter = Bytes("counter") # int

        op_increment = Bytes("inc")
        op_decrement = Bytes("dec")

        increment = Seq(
            [
                App.globalPut(global_counter, App.globalGet(global_counter) + Int(1)),
                Approve(),
            ]
        )

        decrement = Seq(
            [
                App.globalPut(global_counter, App.globalGet(global_counter) - Int(1)),
                Approve(),
            ]
        )

        return program.event(
            init=Seq(
                App.globalPut(global_counter, Int(0)),
                App.globalPut(global_owner, Txn.sender()),
                Approve(),
            ),
            no_op=Cond(
                [Txn.application_args[0] == op_increment, increment],
                [Txn.application_args[0] == op_decrement, decrement],
            ),
        )

    def clear():
        return Approve()

Commands:

    ./sandbox enter algod


    ONE=F5SVYACBT4LX6PHNS5RWJJPX2K462PQETQJOJENRR2QY3VJ2AKUOX2EHRM

    goal app create \
        --creator $ONE \
        --approval-prog /data/build/approval.teal \
        --clear-prog /data/build/clear.teal \
        --global-byteslices 1 \
        --global-ints 1 \
        --local-byteslices 0 \
        --local-ints 0


    goal app info --app-id 2

    goal app read --global --app-id 2
    goal app read --global --app-id 2 --guess-format



    goal app call --app-id 2 --from $ONE --app-arg "str:inc"
    goal app call --app-id 2 --from $ONE --app-arg "str:inc"
    goal app call --app-id 2 --from $ONE --app-arg "str:inc"

    goal app read --global --app-id 2 --guess-format

    goal app call --app-id 2 --from $ONE --app-arg "str:dec"

    goal app read --global --app-id 2 --guess-format

## VIDEO 6

Debugging:

    goal app call --app-id 2 --from $ONE --app-arg "str:inc" --dryrun-dump -o tx.dr


## VIDEO 7

Debugging
