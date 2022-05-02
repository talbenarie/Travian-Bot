from random import randrange

from application import Bot
from time import sleep
import sys


def main():
    if len(sys.argv) > 8:
        print("You did not write the correct system variables")
        return

    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    targets = sys.argv[4].split(",")
    min = sys.argv[5]
    max = sys.argv[6]

    bot = Bot.Bot(url, username, password)
    bot.login()
    bot.go_home()

    while True:
        bot.send_list(targets, randrange(int(min), int(max)))
        bot.go_home()


if __name__ == "__main__":
    main()
    sleep(5)
