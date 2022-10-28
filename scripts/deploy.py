from brownie import network, FundMe, MockV3Aggregator, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    # need to pass appropriate price feed address to the .deploy() method
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # FundMe.deploy({'from': account}, publish_source=config['networks'][network.show_active()]['verify']) also works
    # but the below is more forgiving if you don't have a verify: on one of the networks in the .yaml
    fund_me = FundMe.deploy(price_feed_address, {'from': account},
                            publish_source=config['networks'][network.show_active()].get('verify'))
    print(f'Contract deployed to {fund_me.address}')
    return fund_me


def main():
    deploy_fund_me()
