#!/usr/bin/env python3

from web3 import Web3, HTTPProvider
import json
import os
from sh import seth
import rlp
import hashlib

from ethereum.utils import mk_contract_address, sha3, normalize_address, encode_hex


C = {'ROPSTEN': os.environ['ROPSTEN'], 'MAIN': os.environ['MAINNET'] ,'TEST': 'HTTP://127.0.0.1:7545'}



# Seperates rpc uri address to seperate address an port 
def addr_port(var):

    s = var.split(':')
    addr = s[0]+':'+s[1]
    port = s[-1]
    return addr, port


def build_command(inputs):

    for mem in inputs:
        if type(mem) == type(list):
            print ()
    
            c_list.append()
            
        if type(mem) == type('s'):
            print ()

    return 

if __name__=='__main__':

    addr, port = addr_port(C['TEST'])

    print (seth('--rpc-host', addr, '--rpc-port', port, 'age'))
  
    commands = ['--rpc-host', addr, '--rpc-port', port]
    
    a = '0x627306090abaB3A6e1400e9345bC60c78a8BEf57' 

    #print (seth('--rpc-host', addr, '--rpc-port', port,
    #            'balance', a))


    for i in range(3):
        print(encode_hex(mk_contract_address('0xad997147b38683442d7191bA052b729351bFA308', i)))
       
            
        
