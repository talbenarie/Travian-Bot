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

    if not bot.is_logged():
        print('Incorrect username and password')
        return

    bot.go_home()

    while True:
        try:
            bot.send_list(targets)
        except Exception as e:
            print('Failed to send farm list')
            if not bot.is_logged():
                bot.login()

        # stay inside farm list for 1/3 of the delay time (to see attack send list)
        delay = randrange(int(min), int(max))
        partial_delay = delay / 3
        delay -= partial_delay

        # sleep inside farm list, after that go to village and rest inside
        sleep(partial_delay)
        bot.go_village()
        sleep(delay)


if __name__ == "__main__":
    main()
    sleep(5)
