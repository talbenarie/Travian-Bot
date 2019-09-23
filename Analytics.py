from datetime import datetime
import codecs


class Analytics:
    line_diff = "#############"
    line_breaker = "~"
    file_suffix = ".log"

    def __init__(self, name="analytics"):
        self.filename = name + self.file_suffix
        self.text = "\n" + self.line_diff + "\n"
        self.add_line("time~" + str(datetime.now()))

    def add_info(self, arr):
        txt = ""
        for i in arr:
            txt += i.text + self.line_breaker

        self.add_line(txt)

    def add_line(self, line):
        self.text += str(line) + "\n"
        print(str(line))

    def submit(self):
        file = codecs.open(self.filename, "a+", "utf-8")
        file.write(str(self.text))
        file.close()

