# import requests

# # Адрес REST API для фьючерсов Bybit V5
# url = "https://api.bybit.com/v5/market/orderbook"

# # Параметры запроса: символ и глубина
# params = {
#     "category": "spot",  # фьючерсы USDT
#     "symbol": "BTCUSDT",
#     "limit": 300  # количество уровней стакана
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     bids = data['result']['b']
#     asks = data['result']['a']


#     min_size = 1

#     large_bids = [order for order in bids if float(order[1]) >= min_size]
#     large_asks = [order for order in asks if float(order[1]) >= min_size]

#     print("Крупные заявки на покупку:")
#     for price, size in large_bids:
#         print(f"Цена: {price}, Объем: {size}")

#     print("\nКрупные заявки на продажу:")
#     for price, size in large_asks:
#         print(f"Цена: {price}, Объем: {size}")

# else:
#     print("Ошибка при запросе:", response.text)
# print(f'sell: {large_bids}')
# print(f'buy: {large_asks}')
#
# import matplotlib.pyplot as plt
# import numpy as np

# Примерные данные
# prices = np.linspace(10000, 11000, 100)
# volumes = np.linspace(0, 500, 50)
# heat_data = np.random.rand(50, 100) * 100

# plt.figure(figsize=(10, 6))
# plt.imshow(
#     heat_data,
#     aspect="auto",
#     origin="lower",
#     extent=[prices.min(), prices.max(), volumes.min(), volumes.max()],
#     cmap="viridis",
# )  # Цветовая схема: viridis, hot, plasma и т.д.

# plt.colorbar(label="Order Density")
# plt.xlabel("Price")
# plt.ylabel("Volume")
# plt.title("Order Book Heatmap")
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# heat_data = np.random.rand(50, 100) * 100

# plt.figure(figsize=(10, 6))
# sns.heatmap(heat_data, cmap="viridis")

# plt.title("Order Book Heatmap")
# plt.xlabel("Price")
# plt.ylabel("Volume")
# plt.show()

# import matplotlib.pyplot as plt

# # Пример данных
# order_levels = [
#     {"price": 10050, "volume": 10},
#     {"price": 10075, "volume": 25},
#     {"price": 10100, "volume": 50},
#     {"price": 10125, "volume": 30},
#     {"price": 10150, "volume": 5},
# ]

# # Настроим размер графика
# plt.figure(figsize=(10, 6))

# for level in order_levels:
#     price = level["price"]
#     volume = level["volume"]

#     # Нарисовать горизонтальную линию на уровне цены
#     plt.hlines(y=price, xmin=0, xmax=volume, colors="blue", linewidth=2)

# # Подписать оси
# plt.xlabel("Volume")
# plt.ylabel("Price")

# # Инвертировать ось Y, если нужно чтобы цена шла вверх
# plt.gca().invert_yaxis()

# plt.title("Order Levels")
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Пример данных
order_levels = [
    {"price": 10050, "volume": 10, "side": "bid"},
    {"price": 10075, "volume": 25, "side": "ask"},
    {"price": 10100, "volume": 50, "side": "bid"},
    {"price": 10125, "volume": 30, "side": "ask"},
    {"price": 10150, "volume": 5, "side": "bid"},
]

# Найдем максимальный объем, чтобы нормализовать цвета и толщины
max_volume = max(level["volume"] for level in order_levels)

# Настроим фигуру
plt.figure(figsize=(10, 6))

for level in order_levels:
    price = level["price"]
    volume = level["volume"]
    side = level["side"]

    # Цвета базовые для bid/ask
    base_color = "green" if side == "bid" else "red"

    # Нормализуем интенсивность цвета по объему
    norm_intensity = volume / max_volume  # От 0 до 1
    color = mcolors.to_rgba(
        base_color, alpha=0.3 + 0.7 * norm_intensity
    )  # прозрачность от 0.3 до 1

    # Толщина линии пропорциональна объему
    linewidth = 1 + 4 * norm_intensity  # от 1 до 5 пикселей

    plt.hlines(y=price, xmin=0, xmax=volume, colors=[color], linewidth=linewidth)

plt.xlabel("Volume")
plt.ylabel("Price")
plt.gca().invert_yaxis()
plt.title("Order Book Levels (Volume -> Color & Width)")
plt.grid(True)
plt.show()
