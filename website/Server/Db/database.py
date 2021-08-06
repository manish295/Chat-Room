import sqlite3
from sqlite3 import Error



class Database:

    def __init__(self):
        self.conn = sqlite3.connect('website\Server\Db\messages.db', isolation_level=None)
        # self.conn.execute("PRAGMA journal_mode=WAL;")
        self.c = self.conn.cursor()
        # self.c.execute("PRAGMA journal_mode=WAL;")

    def save_messages(self, name, message):
        self.c.execute(f"INSERT INTO messages VALUES ('{name}', '{message}')")
        # self.conn.commit()
    
    def close(self):
        self.conn.close

    def remove_messages(self, name=True):
        if name == True:
            self.c.execute("DELETE FROM messages")
            # self.conn.commit()
        else:
            self.c.execute(f"DELETE FROM messages WHERE name='{name}'")
            # self.conn.commit()

    def return_messages(self, name, all=False):
        if all:
            self.c.execute(f"SELECT * FROM messages")
            vals = self.c.fetchall()
            # self.conn.commit()
            results = []
            for val in vals:
                data = {"name": val[0], "message": val[1]}
                results.append(data)

            return results
        else:
            self.c.execute(f"SELECT * FROM messages WHERE name='{name}'")
            vals = self.c.fetchall()
            # self.conn.commit()
            return vals
    


    
    




# writedb = WriteDatabase()
# writedb.save_messages("Manish", "Hello!")

# readdb = ReadDatabase()
# print(readdb.return_messages("Manish", all=True))






    


        



# conn = sqlite3.connect('website\Db\messages.db')

# c = conn.cursor()

# # c.execute("""CREATE TABLE messages (
# #              name text,
# #              message text

# #             )""")


# c.execute("INSERT INTO messages VALUES ('Manish', 'Hello!')")


# # c.execute("SELECT * FROM messages WHERE message='Hello!'")

# # print(c.fetchone())

# conn.commit()


# conn.close

