# models/database.py
import sqlite3

class Database:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connection = sqlite3.connect("library.db", check_same_thread=False)
        return cls._instance

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect("library.db", check_same_thread=False)
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None
