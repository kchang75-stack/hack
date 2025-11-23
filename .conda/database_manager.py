import sqlite3
import pandas as pd

class DatabaseManager:

    @staticmethod
    def create_database(item_list, database_name):

        conn = sqlite3.connect(database_name + ".db")
        cur = conn.cursor()

        cur.execute(f"DROP TABLE IF EXISTS {database_name}")
        first_dict = item_list[0]
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {database_name} (itemName TEXT, itemPrice REAL, storeName TEXT, query TEXT)"

        cur.execute(create_table_sql)

        column_names = ", ".join(first_dict.keys())
        placeholders = ", ".join(["?" for _ in first_dict.keys()])

        insert_sql = f"INSERT INTO {database_name} ({column_names}) VALUES ({placeholders})"

        rows = [tuple(item.values()) for item in item_list]

        cur.executemany(insert_sql, rows)

        conn.commit()

        conn.close()
        
        return (database_name + ".db") # returns database file name

    @staticmethod
    def get_cheapest_by_product(database):
        conn = sqlite3.connect(database + ".db")
        cur = conn.cursor()
        query = f"""
            SELECT p.*
            FROM products p
            JOIN (
                SELECT itemName, MIN(itemPrice) AS minPrice
                FROM {database}
                GROUP BY query
            ) m
            ON p.itemName = m.itemName AND p.itemPrice = m.minPrice
            ORDER BY p.itemName ASC
        """

        cur.execute(query)

        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod   
    def get_prices_by_product(database, queryVal):
        conn = sqlite3.connect(database + ".db")
        cur = conn.cursor()

        query = f"""
            SELECT itemName, itemPrice, storeName, query
            FROM {database}
            WHERE itemName = ?
            ORDER BY itemPrice ASC
        """

        cur.execute(query, (queryVal,))
        result = cur.fetchmany(5)
        conn.close()
        return result

    @staticmethod
    def convert_to_df(database_name):
        conn = sqlite3.connect(database_name + ".db")
        return pd.read_sql_query(f"SELECT * from {database_name}", conn)


