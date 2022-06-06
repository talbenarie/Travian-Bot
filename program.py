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
        failed = False

        print('Attacking..')

        try:
            bot.send_list(targets)
        except Exception as e:
            print('Failed to send farm list')
            if not bot.is_logged():
                bot.login()
            failed = True

        # declare time left until next time of sending farm list
        delay = randrange(int(min), int(max))

        # upon failure, delay time will be cut by half
        if failed:
            delay /= 2

        # declare time spent looking on the farm list
        delay_list_post_attack = randrange(60, 180)
        delay_list_pre_attack = randrange(30, 90)

        # remove time spent from total delay
        delay -= delay_list_post_attack
        delay -= delay_list_pre_attack

        # declare time spent staying at the village & home
        delay_village = int(delay / 2)
        delay_home = delay_village

        # execute orders
        sleep(delay_list_post_attack)

        print('Rest time begins, you have got ' + str(delay_village + delay_home) + " seconds to do stuff")
        bot.go_village()
        sleep(delay_village)
        bot.go_home()
        sleep(delay_home)

        # enter farm list without attacking, to show user farmlist will be sent soon
        print('Rest is over, preparing attack in ' + str(delay_list_pre_attack) + " seconds")
        bot.go_farmlist()
        sleep(delay_list_pre_attack)


if __name__ == "__main__":
    main()
    sleep(5)
