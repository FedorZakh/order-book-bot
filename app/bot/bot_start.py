import requests
import time
from data_req.queries import DatabaseManager

db = DatabaseManager("database.db")

url = "https://api.bybit.com/v5/market/orderbook"

params = {
    "category": "spot",
    "symbol": "BTCUSDT",
    "limit": 200,
}

# parameter = "continue"
parameter = "start"


def order_bot():
    response = requests.get(url, params=params)
    count = 0

    if parameter == "start":
        db.delete_database()
        db.create_table_orders()
        while True:
            if response.status_code == 200:
                data = response.json()
                bids = data["result"]["b"]
                asks = data["result"]["a"]
                name = data["result"]["s"]
                min_size = 0.05
                large_bids = [order for order in bids if float(order[1]) >= min_size]
                large_asks = [order for order in asks if float(order[1]) >= min_size]
                for i in large_bids:
                    db.add_order_buy(name, i[1], i[0])
                for i in large_asks:
                    db.add_order_sell(name, i[1], i[0])

            count += 1
            print(count)
            time.sleep(5)

    elif parameter == "continue":
        while True:
            print("тестовый режим")
            time.sleep(5)
