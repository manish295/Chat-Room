import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

"""
Connect to postgreSQL database
Create a table if it doesn't exist
Handle storing, removing, and returning messages 
"""
class Database:

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute(''' CREATE TABLE IF NOT EXISTS messages (
                                    id      serial PRIMARY KEY NOT NULL,
                                    name    text,
                                    message text)''')
            self.conn.commit()
        except Exception as err:
            print(err)
            self.close()
    def add_message(self, name, message):
        try:
            self.cursor.execute(f"INSERT INTO messages(name, message) VALUES ('{name}', '{message}')")
            self.conn.commit()
        except Exception as err:
            print(err)
            self.close()
            
    
    def return_messages(self):
        try:
            self.cursor.execute("select name, message from messages")
            rows = self.cursor.fetchall()
            results = []
            for r in rows:
                results.append(r[1])
            return results
        except Exception as err:
            print(err)
            self.close()

    
    def remove_messages(self):
        try:
            self.cursor.execute("DELETE FROM messages")
            self.conn.commit()
        except Exception as err:
            print(err)
            self.close()

    
    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
