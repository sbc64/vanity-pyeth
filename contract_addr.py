#!/usr/bin/env python3

import os
import ast
from ethereum.utils import (
        mk_contract_address,
        sha3,
        normalize_address,
        encode_hex,
        privtoaddr,
        checksum_encode
    )

def generate_pk():
    
    pk = sha3(os.urandom(4096))

    return encode_hex(pk)


if __name__=='__main__':

    # VARS
    to_generate = 10
    contracts_to_gen = 3


    keys_dict_list = []
    for x in range(to_generate):
        keys_dict_list.append({"pk": generate_pk()})

    for member in keys_dict_list:
        a = checksum_encode(privtoaddr(member['pk']))
        member['pa'] = a

    
    for member in keys_dict_list:
        contracts = []
        for i in range(contracts_to_gen):
            c_addr_ = str(encode_hex(mk_contract_address(member['pa'], i)))
            contracts.append("0x" + c_addr_.replace("\'",""))

        member['contracts'] = contracts 

    
    for m in keys_dict_list:
        print (m)
        print ()

