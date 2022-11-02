from selenium import webdriver
from time import sleep
import pathlib

scriptDirectory = pathlib.Path().absolute()


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f"user-data-dir={scriptDirectory}\\Perfil")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def access(self, url):
        self.chrome.get(url)

    def get_player_name(self):
        player_name = self.chrome.find_element_by_css_selector(
            '#main-view > ms-widget-layout > ms-widget-slot > ms-tabbed-grid-widget > ms-grid > ms-event-group > ms-event:nth-child(2) > div > a > ms-event-detail > ms-event-name > ms-inline-tooltip > div > div:nth-child(2) > div > div'
        )
        player_name_html = player_name.get_attribute('innerHTML')
        print(player_name_html)


if __name__ != '__main__':
    chrome = ChromeAuto()
    chrome.access('https://sports.sportingbet.com/en/sports/tennis-5')


import requests
from bs4 import BeautifulSoup

url = 'https://sports.sportingbet.com/en/sports/tennis-5'
response = requests.get(url)

# Se formos usar "post", é necessário colocar o parametro "data" com os dados para o post
html = BeautifulSoup(response.text, 'html.parser')

for event in html.select('.grid-event-detail'):
    print('found...')
    print(event)


