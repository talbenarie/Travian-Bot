import mysql.connector


class Database:
    def __init__(self, db_host, db_name, db_user, db_pass):
        self.db = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            passwd=db_pass
        )

        self.cursor = self.db.cursor()

    def update(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
