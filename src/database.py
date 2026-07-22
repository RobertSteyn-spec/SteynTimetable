import sqlite3


class Database:
    def __init__(self):
        print("Opening database...")

        self.connection = sqlite3.connect("steyn_timetable.db")
        self.cursor = self.connection.cursor()

        print("Database opened successfully.")

    def close(self):
        self.connection.close()