from datetime import time
import codecs
from Database import Database
import time


class Analytics:
    def __init__(self):
        self.database = Database("localhost", "travian_analytics", "root", "")
        self.current_timestamp = str(time.time())

    def add_info(self, arr):
        if len(arr) == 1:
            return

        rank = 0
        name = ""
        points = 0

        for i in range(len(arr)):
            if i == 0:
                s = arr[i].text
                s.replace(".", "")
                s.replace(" ", "")
                rank = str(int(float(s)))
            elif i == 1:
                name = arr[i].text
            elif i == 2:
                s = arr[i].text
                points = str(int(float(s)))

        self.database.update("INSERT INTO raid_analytics (`timestamp`, `rank`, `name`, `points`) VALUES (" + self.current_timestamp + ", " + rank + ", '" + name + "', " + points + ")")

