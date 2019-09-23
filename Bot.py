from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Logger
import random
import Analytics
from time import sleep


release = True  # if release = false means its being tested, bot wont sleep


class GameBot:
    browser = None
    executable_path = "source/webdriver/chromedriver"
    logger = Logger.Logger("Logger")
    raid_analytics = Analytics.Analytics("raid_analytics")

    def __init__(self, url, username, password, lang="en"):
        self.url = url
        self.username = username
        self.password = password
        self.raid_text = self.get_raid_text(lang)

    def start(self):
        self.browser = webdriver.Chrome(executable_path=self.executable_path)
        self.browser.get(self.url)
        sleep(1)

    def login(self):
        self.random_sleep(0, 300)
        self.browser.find_element_by_name("name").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        self.browser.find_element_by_name("s1").click()  # Submit form
        self.logger.add_line("Logging into: " + self.username)
        sleep(1)

    def enter_top_players(self):
        self.browser.get(self.url + "statistiken.php?id=0&idSub=3")
        self.logger.add_line("entering top players")
        sleep(1)

    def grab_raider_table(self):
        table = self.browser.find_element_by_id("top10_raiders")  # raiders table
        rows = table.find_elements_by_tag_name("tr")  # teg all of the rows
        rows.pop(0)
        for row in rows:
            col = row.find_elements_by_tag_name("td")
            self.raid_analytics.add_info(col)

    def record_raider_rank(self):
        self.enter_top_players()
        self.grab_raider_table()
        self.raid_analytics.submit()

    def enter_village(self):
        self.browser.get(self.url + "dorf2.php")
        self.logger.add_line("entering village")  # do something
        sleep(1)

    def enter_rally_point(self):
        self.browser.find_element_by_class_name("g16").click()
        self.logger.add_line("entering rally point")  # do something
        sleep(1)

    def enter_farm_list(self):
        self.browser.find_element_by_class_name("favorKey99").click()
        self.logger.add_line("entering farm list")
        sleep(1)

    def send_farm_list(self, index):
        self.random_sleep(1, 60)
        checkboxes = self.browser.find_elements_by_xpath("//input[contains(@class, 'markAll') "
                                                         "and contains(@class, 'check')]")

        if len(checkboxes) <= index:
            self.logger.add_line("Index is out of checkboxes bounds: " + str(len(checkboxes)))
            return

        checkboxes[index].send_keys(Keys.SPACE)
        buttons = self.browser.find_elements_by_xpath("//button[contains(text(),'" + self.raid_text + "')]")
        if len(buttons) <= index:
            self.logger.add_line("Index is out of button bounds: " + str(len(buttons)))
            return

        buttons[index].click()
        self.logger.add_line("Sent attack on index: " + str(index))
        sleep(2)

    def send_attacks(self, array):
        self.enter_village()
        self.random_sleep(0, 600)
        self.enter_rally_point()
        self.enter_farm_list()
        for i in array:
            self.send_farm_list(int(i))

    def submit(self):
        self.logger.submit()

    def submit_error(self):
        self.logger.add_line("There was an exception during runtime")
        self.logger.submit()

    def random_sleep(self, min_num, max_num):
        if not release:
            return
        sleep_time = random.randint(min_num, max_num)
        self.logger.add_line("sleeping for extra " + str(sleep_time) + " seconds")
        sleep(sleep_time)

    @staticmethod
    def get_raid_text(lang):
        if lang == 'en':
            return "Start raid"
        elif lang == "he":
            return "שלח בזיזה"

