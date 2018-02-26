#!/usr/bin/env python3

import os
import ast
import argparse
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

# generates a single private and public dict
def private_and_pub():

    pk = generate_pk()
    return {'pk': pk,
            'pa': checksum_encode(privtoaddr(pk))}
    
def only_keys(quantity):

    for x in range(to_generate):
        print (private_and_pub()) 
        print ()

def check_hex_str(string):

    # can't get string.hexdigits to work
    if not (all(c in '0123456789abcdefABCDEF' for c in string)):
        raise("Not a hexadecimal string")


def vanity_contracts(quantity_of_contracts, vanity):
   
    check_hex_str(vanity)
    nonce_count = 0
    pk = generate_pk()

    while True:
            
        contract = generate_contracts(1, pk, nonce_count)[0]
            
        if vanity == contract[2:2+len(vanity)]:
            nonce_count += 1
            if nonce_count == quantity_of_contracts:
                break

        else:
            pk = generate_pk()
            nonce_count = 0

    return (pk)

# Generates the contracts address from given private key
def generate_contracts(quantity_per_key, private_key, nonce=0):
    
    pa = checksum_encode(privtoaddr(private_key))
    
    contracts = []
    for i in range(quantity_per_key):
        c_addr_ = str(encode_hex(mk_contract_address(pa, i + nonce)))
        contracts.append("0x" + c_addr_.replace("\'",""))

    return contracts

if __name__=='__main__':


    parser = argparse.ArgumentParser(
            description='Ethereum contract address generator, can also generate private keys')

    parser.add_argument('-pk',
                        '--private-key',
                        dest="SUPPLIED_KEYS",
                        default='',
                        nargs='*',
                        type=str,
                        help="private key to use for generating contract addresses"
                       )

    parser.add_argument('-n',
                        '--nonce',
                        dest="NONCE",
                        type=int,
                        default=0,
                        help="nonce of the privided private key"
                        )

    parser.add_argument('-q',
                        '--quantity',
                        dest="C_TO_GEN",
                        type=int,
                        default=1,
                        help="quantity of contracts to generate or quantiy of keys if -k flag is used"
                        )

    parser.add_argument('-V',
                        '--vanity',
                        dest="VANITY_STR",
                        type=str,
                        default='',
                        help="""vanity chars in the contracts addresses.\n
                              WARNING: more than four chars will increase duration by A LOT

                              """
                        )

    parser.add_argument('-k',
                        '--keys',
                        dest="ONLY_KEYS",
                        action='store_true'
                        )


    try:
        args = parser.parse_args()
    except:
        exit(2)

    # VARS
    to_generate = args.C_TO_GEN
    contracts_to_gen = args.C_TO_GEN
    nonce = args.NONCE

    if args.ONLY_KEYS:
        only_keys(quantity=args.C_TO_GEN)
        exit(0)
    
    if args.VANITY_STR:
        pk = vanity_contracts(args.C_TO_GEN, args.VANITY_STR)
        c = generate_contracts(args.C_TO_GEN, pk)
        print ("pk: {}\ncontracts: {}".format(pk, c))
        exit(0)

    if args.SUPPLIED_KEYS:
        for pk in args.SUPPLIED_KEYS:
            contracts = generate_contracts(args.C_TO_GEN, pk)
            
            print ('\npk: {} \ncontracts: {}\n\n'.format(pk, contracts))
        exit(0)
