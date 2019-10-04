import mysql.connector


class Database:
    def __init__(self, db_host, db_name, db_user, db_pass):
        try:
            self.db = mysql.connector.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                passwd=db_pass
            )
            self.connected = True
        except Exception:
            print("cannot connect to mysql service")
            self.connected = False
            return

        self.cursor = self.db.cursor()

    def update(self, sql):
        if not self.connected:
            return
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, sql):
        if not self.connected:
            return
        self.cursor.execute(sql)
        return self.cursor.fetchall()
