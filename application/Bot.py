from random import randrange

from application import Chrome
from time import sleep
from datetime import datetime


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


class Bot:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.browser = Chrome.Chrome()

    def login(self):
        self.browser.goto(self.url)
        sleep(randrange(3, 5))
        self.browser.post({'name': self.username, 'password': self.password})
        sleep(randrange(1, 5))
        self.browser.click('textButtonV1.green')
        sleep(randrange(1, 5))
        print('Logged into the account ' + self.username)

    def go_home(self):
        self.browser.goto(self.url + 'dorf1.php')

    def go_village(self):
        self.browser.goto(self.url + 'dorf2.php')

    def send_list(self, list):
        self.browser.goto(self.url + 'build.php?id=39&gid=16&tt=99')
        sleep(randrange(3, 5))
        buttons = self.browser.get_buttons('textButtonV1.green')
        for i in range(len(list)):
            index = int(list[i])
            buttons[index].click()
            print('List #' + str(index) + ' were sent')
            sleep(randrange(3, 5))

        print(get_time() + ': Lists were sent')

    def is_logged(self):
        return self.browser.current_url() != self.url
