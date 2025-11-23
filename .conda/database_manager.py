import sqlite3
import pandas as pd

class DatabaseManager:

    @staticmethod
    def create_database(item_list, table):

        conn = sqlite3.connect("prices.db")
        cur = conn.cursor()

        cur.execute(f"DROP TABLE IF EXISTS {table}")
        first_dict = item_list[0]
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table} (itemName TEXT, itemPrice REAL, storeName TEXT, query TEXT)"

        cur.execute(create_table_sql)

        column_names = ", ".join(first_dict.keys())
        placeholders = ", ".join(["?" for _ in first_dict.keys()])

        insert_sql = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

        rows = [tuple(item.values()) for item in item_list]

        cur.executemany(insert_sql, rows)

        conn.commit()

        conn.close()
        
        return ("prices.db") # returns database file name

    @staticmethod
    def get_cheapest_by_product(table):
        conn = sqlite3.connect("prices.db")
        cur = conn.cursor()
        query = f"""
            SELECT t.*
            FROM {table} t
            JOIN (
                SELECT "query", MIN(itemPrice) AS minPrice
                FROM {table}
                GROUP BY "query"
            ) m
            ON t.query = m.query AND t.itemPrice = m.minPrice
            ORDER BY t.itemName ASC
        """

        cur.execute(query)

        result = cur.fetchall()
        cur.close()
        return result


    @staticmethod   
    def get_prices_by_product(table_name, product):
        conn = sqlite3.connect("prices.db")
        cur = conn.cursor()

        # Safely quote table name
        query = f"""
            SELECT itemName, itemPrice, storeName, "query"
            FROM "{table_name}"
            WHERE "query" = ?
            ORDER BY itemPrice ASC
        """

        cur.execute(query, (product,))
        result = cur.fetchmany(10)
        conn.close()
        return result
    # @staticmethod   
    # def get_prices_by_product(table, queryVal):
    #     conn = sqlite3.connect("prices.db")
    #     cur = conn.cursor()

    #     query = f"""
    #         SELECT itemName, itemPrice, storeName, "query"
    #         FROM {table}
    #         WHERE "query" = ?
    #         ORDER BY itemPrice ASC
    #     """

    #     cur.execute(query, (queryVal,))
    #     result = cur.fetchmany(10)
    #     conn.close()
    #     return result

    @staticmethod
    def convert_to_df(table):
        conn = sqlite3.connect("prices.db")
        return pd.read_sql_query(f"SELECT * from {table}", conn)


