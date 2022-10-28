from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local', 'ganache-loc']


def get_account():
    # network keyword was imported and has a show_active() method: brownie.network.show_active()
    # if the active network is a development network use the first account from our ganache list
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    # otherwise check our brownie-config.yaml file for the wallet there
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    # if it is development we will need to deploy our mock aggregator which we placed in our contracts/test folder
    print(f'The active network is {network.show_active()}')
    print('Deploying Mocks...')
    if len(MockV3Aggregator) >= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from': get_account()})
    print('Mocks deployed!')

