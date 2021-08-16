import sqlite3


"""
Connect to specified database
If database/table not found/created, create a table
A new database is automatically created if db file is not present
Handle storing, removing, and returning messages
"""
class Database:

    
    def __init__(self):
        self.conn = sqlite3.connect('website\messages.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.c.fetchall()
        if "messages" not in tables[0]:
            self.c.execute("""CREATE TABLE messages (
                            name text,
                            message text
            )""")


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

    def return_messages(self, name=None, all=True):
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
