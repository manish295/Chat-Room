import sqlite3
from sqlite3 import Error



class Database:

    def __init__(self):
        self.conn = sqlite3.connect('website\Db\messages.db', check_same_thread=False)
        # self.conn.execute("PRAGMA journal_mode=WAL;")
        self.c = self.conn.cursor()
        # self.c.execute("PRAGMA journal_mode=WAL;")

    def save_messages(self, name, message):
        self.c.execute(f"INSERT INTO messages VALUES ('{name}', '{message}')")
        self.conn.commit()
    
    def close(self):
        self.conn.close

    def remove_messages(self, table, values=True):
        if values == True:
            self.c.execute(f"DELETE FROM {table}")
            self.conn.commit()
        elif table == "messages":
            self.c.execute(f"DELETE FROM {table} WHERE name='{values}'")
            self.conn.commit()
        else:
            self.c.execute(f"DELETE FROM {table} WHERE key='{values}'")

    def return_messages(self, name, all=False):
        if all:
            self.c.execute(f"SELECT * FROM messages")
            vals = self.c.fetchall()
            self.conn.commit()
            results = []
            for val in vals:
                results.append(val[1])

            return results
        else:
            self.c.execute(f"SELECT * FROM messages WHERE name='{name}'")
            vals = self.c.fetchall()
            self.conn.commit()
            return vals

    


# db = Database()
# db.remove_messages("messages")
# db.close()

