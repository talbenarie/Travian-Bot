import Bot
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

url = "https://tsx.travian.x/"
username = "username"
password = "password"
language = "en"
targets = [0, 1, 2]


def main():
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

