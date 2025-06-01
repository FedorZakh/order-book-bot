import requests
import time
from app.data_req.queries import DatabaseManager

db = DatabaseManager("database.db")

url = "https://api.bybit.com/v5/market/orderbook"

params = {
    "category": "spot",
    "symbol": "BTCUSDT",
    "limit": 300,
}

parameter = "continue"
# parameter = "start"


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

                min_size = 1

                large_bids = [order for order in bids if float(order[1]) >= min_size]
                large_asks = [order for order in asks if float(order[1]) >= min_size]

                print("Крупные заявки на покупку:")
                for price, size in large_bids:
                    print(f"Цена: {price}, Объем: {size}")

            print("\nКрупные заявки на продажу:")
            for price, size in large_asks:
                print(f"Цена: {price}, Объем: {size}")

            else:
                print("Ошибка при запросе:", response.text)
                print(f"sell: {large_bids}")
                print(f"buy: {large_asks}")
            count += 1
            print(count)
            time.sleep(3)
    elif parameter == "continue":
        while True:
            print("тестовый режим продолжение")
            time.sleep(3)
