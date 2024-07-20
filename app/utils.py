import requests 

def getBlockNumber(inputNumber):
    url = 'https://eth-mainnet.public.blastapi.io/'
    json_data = {
                    "jsonrpc":"2.0",
                    "method":"eth_blockNumber",
                    "id":inputNumber
                }
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.get(url,json=json_data, headers= headers)
    blockNumber = response.json()['result']
    return blockNumber


def getTransactions(blockNumber, inputNumber):
    print(blockNumber)

    url = 'https://eth-mainnet.public.blastapi.io/'
    json_data = {   
        "jsonrpc":"2.0",
        "method":"eth_getBlockByNumber",
        "params":[blockNumber,True],
        "id": inputNumber
    }
    
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.get(url,json=json_data,headers= headers)
    result = response.json()['result']['transactions']

    trimmed_data = [
    {
        "hash": item["hash"],
        "value": item["value"],
        "from": item["from"],
        "to": item["to"],
        "r": item["r"],
        "s": item["s"]
    }
    for item in result
]

    return trimmed_data