# pip install web3
# correct error get_block

from web3 import Web3
from web3.middleware import geth_poa_middleware 

API_url = "https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98" #predefined
web3 = Web3(Web3.HTTPProvider(API_url)) 

Block_data = web3.eth.get_block(12964964) # any block can be taken
print('Block data:',Block_data )

print('gasUsed:',Block_data ['gasUsed'])
print('Total difficulty:',Block_data ['difficulty'])

print('transaction data',Block_data['transactions']) 
transaction = web3.eth.get_transaction('0x4121669c46c143d17eb2233c8cd73ef52125cb5f0e352bac13093a628f958890')
print('data',transaction)

