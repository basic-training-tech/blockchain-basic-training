from pyteal import *
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
        # no_op=,
    )

def clear():
    return Approve()
