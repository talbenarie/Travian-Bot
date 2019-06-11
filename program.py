import Bot
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
import sys


def main():
    if len(sys.argv) > 6:
        print("You did not write the correct system variables")
        return

    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    language = sys.argv[4]
    targets = sys.argv[5].split(",")

    bot = Bot.GameBot(url, username, password, language)
    try:
        bot.start()
        bot.login()
        bot.send_attacks(targets)
        bot.submit()
    except ElementClickInterceptedException:
        bot.submitError()

    sleep(5)


if __name__ == "__main__":
    main()

