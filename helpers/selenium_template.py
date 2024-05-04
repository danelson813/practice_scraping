from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep


# url = "https://scrapeme.live/shop/"


def get_soup(url_):
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent:{user_agent}')
    with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("homepage.png")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return soup

