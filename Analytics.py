from datetime import datetime
import codecs


class Analytics:
    line_diff = "#############"
    line_breaker = ","
    file_suffix = ".txt"

    def __init__(self, name="analytics"):
        self.filename = name + self.file_suffix
        self.text = ""

    def start(self):
        self.text = "\n" + self.line_diff + "\n"
        self.add_line(str(datetime.now()))

    def add_info(self, arr):
        if len(arr) == 1:
            return

        txt = ""
        for i in range(len(arr)):
            if i == 0:
                s = arr[i].text
                s.replace(".", "")
                s.replace(" ", "")
                txt += str(int(float(s)))
            else:
                txt += arr[i].text
            if i != len(arr) - 1:
                txt += self.line_breaker

        self.add_line(txt)

    def add_line(self, line):
        self.text += str(line) + "\n"

    def submit(self):
        file = codecs.open(self.filename, "a+", "utf-8")
        file.write(str(self.text))
        file.close()

