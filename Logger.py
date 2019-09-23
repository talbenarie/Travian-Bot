from datetime import datetime


line_diff = "#############"
file_suffix = ".log"


class Logger:
    def __init__(self, filename):
        self.filename = filename + file_suffix
        self.text = "\n" + line_diff + "\n"
        self.add_line("Current Time: " + str(datetime.now()))

    def add_line(self, line):
        self.text += line + "\n"

    def submit(self):
        file = open(self.filename, "a+")
        file.write(self.text)
        file.close()

