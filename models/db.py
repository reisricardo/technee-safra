import mysql.connector
from settings import *

driver = mysql.connector

class database():
    
    def __init__(self):
        self.host = DATABASE_HOST
        self.user = DATABASE_USER
        self.passwd = DATABASE_PASS
        self.port = DATABASE_PORT       
    
    def open_connection(self):
        self.conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port            
        )
        self.cursor = self.conn.cursor(dictionary = True)        
        
        return self.conn, self.cursor

    def close_connection(self, cursor, conn):
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()