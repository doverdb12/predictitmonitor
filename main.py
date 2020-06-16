import json
import requests
import sys
import time

class Contract:
    def __init__(self, id, name, last_trade_price, difference):
        self.id = id
        self.difference = 0
        self.name = name
        self.last_trade_price = last_trade_price
    
    def print_price(self, difference = 0):
        print("name:", self.name, "| price:", self.last_trade_price, "| difference:", self.difference)

class ContractList:
    def __init__(self, contracts):
        self.contracts = contracts

    def find_contract_by_id(self, contract_id):
        for contract in self.contracts:
            if contract.id == contract_id:
                return contract
    
    def print_prices(self, time):
        for c in self.contracts:
            c.print_price(None)
        print("\nRetrieved at:", time, "\n")
    
    def compare_and_update_difference(self, old_contracts):
        for new_contract in self.contracts:
            old_contract = old_contracts.find_contract_by_id(new_contract.id)
            if old_contract:
                new_contract.difference = new_contract.last_trade_price - old_contract.last_trade_price

def build_contract(data):
    return Contract(data.get("id"), data.get("name"), int(data.get("lastTradePrice") * 100), 0)

market_id = sys.argv[1] if len(sys.argv) >= 2 else "5883"
url = "https://www.predictit.org/api/marketdata/markets/" + market_id
poll_time = int(sys.argv[2]) if len(sys.argv) >= 3 else 60

old_contract_list = None
while True:
    r = requests.get(url)
    data = json.loads(r.text)
    contract_list = ContractList(list(map(build_contract, data["contracts"])))
    if old_contract_list:
        contract_list.compare_and_update_difference(old_contract_list)
    contract_list.print_prices(data["timeStamp"])
    old_contract_list = contract_list
    time.sleep(poll_time)