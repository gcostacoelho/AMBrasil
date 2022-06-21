import sqlite3 as sql

class Conexao:
    def __init__(self):
        self.database = "db.db"
        self.conn = None
        self.cur = None
        self.connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms = None):
        if self.connected:
            if parms == None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False