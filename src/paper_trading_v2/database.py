"""
V2 Database Manager
"""

import sqlite3


class Database:

    def __init__(self, db="data/polymarket.db"):

        self.conn = sqlite3.connect(
            db,
            check_same_thread=False
        )

        self.conn.row_factory = sqlite3.Row

    def execute(self, query, params=()):

        cur = self.conn.cursor()

        cur.execute(query, params)

        self.conn.commit()

        return cur

    def fetchone(self, query, params=()):

        cur = self.conn.cursor()

        cur.execute(query, params)

        return cur.fetchone()

    def fetchall(self, query, params=()):

        cur = self.conn.cursor()

        cur.execute(query, params)

        return cur.fetchall()

    def close(self):

        self.conn.close()