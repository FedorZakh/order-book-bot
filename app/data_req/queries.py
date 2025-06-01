import os
import sqlite3 as sq


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def create_table_orders(self):
        with sq.connect(self.db_path) as conn:

            conn.execute(
                """CREATE TABLE IF NOT EXISTS orders_buy (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    value REAL NOT NULL,
                    price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            conn.execute(
                """CREATE TABLE IF NOT EXISTS orders_sell (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    value REAL NOT NULL,
                    price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )

    def add_order_buy(self, name: str, value: float, price: float):
        """Добавляет ордер покупки"""
        with sq.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO orders_buy (name, value, price) VALUES (?,?,?)",
                (name, value, price),
            )

    def add_order_sell(self, name: str, value: float, price: float):
        """Добавляет ордер продажи"""
        with sq.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO orders_buy (name, value, price) VALUES (?,?,?)",
                (name, value, price),
            )

    def delete_database(self):
        """Удаляет файл базы данных"""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            print("База данных удалена.")
        else:
            print("Файл базы не найден.")

    def check_database(self):
        return os.path.exists(self.db_path)
