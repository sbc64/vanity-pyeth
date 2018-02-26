https://github.com/MyEtherWallet/VanityEth

if you want to generate private keys and its respective contract address use the following command:

    ./contract_addr.py -k -q 10 | awk '{print }' | sed 's|,||g' | xargs -I {} ./contract_addr.py -pk {} -q 3


To install deps:

    pip install -r requirements.txt


    usage: contract_addr.py [-h] [-pk [SUPPLIED_KEYS [SUPPLIED_KEYS ...]]]
                        [-n NONCE] [-q C_TO_GEN] [-V VANITY_STR] [-k]

    Ethereum contract address generator, can also generate private keys

    optional arguments:
      -h, --help            show this help message and exit
      -pk [SUPPLIED_KEYS [SUPPLIED_KEYS ...]], --private-key [SUPPLIED_KEYS [SUPPLIED_KEYS ...]]
                        private key to use for generating contract addresses
      -n NONCE, --nonce NONCE
                        nonce of the provided private key
      -q C_TO_GEN, --quantity C_TO_GEN
                        quantity of contracts to generate or quantity of keys
                        if -k flag is used
      -V VANITY_STR, --vanity VANITY_STR
                        vanity chars in the contracts addresses. WARNING: more
                        than four chars will increase duration by A LOT
      -k, --keys            Only generate private keys. Use -q flag for quantity
