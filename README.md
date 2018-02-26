https://github.com/MyEtherWallet/VanityEth

if you want to generate private keys and its respective contract address use the following command:
    ./contract_addr.py -k -q 10 | awk '{print }' | sed 's|,||g' | xargs -I {} ./contract_addr.py -pk {} -q 3


To install deps:

    pip install -r requirements.txt
