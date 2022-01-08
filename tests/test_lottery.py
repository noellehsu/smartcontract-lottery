from brownie import Lottery, network, accounts, config
from web3 import Web3
# 0.013ETH大約130000000000000000wei

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"],
    {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.013,"ether")
    assert lottery.getEntranceFee() <  Web3.toWei(0.022,"ether")


