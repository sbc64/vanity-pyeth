#!/usr/bin/env python3

from web3 import Web3, HTTPProvider
import json
import os
from sh import seth
import rlp
import hashlib
import json
import ast
from ethereum.utils import mk_contract_address, sha3, normalize_address, encode_hex


C = {'ROPSTEN': os.environ['ROPSTEN'], 'MAIN': os.environ['MAINNET'] ,'TEST': 'HTTP://127.0.0.1:7545'}



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



    # Use vanity-eth npm for address generation
    dict_list = []
    with open('addresses', 'r') as addresses:
        for line in addresses:
            
            dict_list.append(ast.literal_eval(line))
            a = dict_list[-1]['address']
            contracts = []

            for i in range(3):
                
                addr_ = str(encode_hex(mk_contract_address(a, i)))
                addr_ = addr_[1:]
                contracts.append("0x"+addr_.replace("\'",""))

            
            dict_list[-1]['contracts'] = contracts
        
        with open('output', 'w+') as out:
           
            for x in dict_list:
               
                out.write(str(x))
                out.write("\n\n")

        
