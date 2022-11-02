"""
Selenium
14/02/2022

Selenium teve uma atualização recentemente. O que mudou?
"""
from pathlib import Path
# Poderiamos também utilizar o os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import selenium

print(selenium.__version__)

root_folder = Path(__file__).parent.parent.parent
# parent serve para pegar o folder anterior

chrome_driver_path = Path(__file__).parent.parent / 'chromedriver.exe'
# o chrome driver deve estar especificado no caminho correto!
print(chrome_driver_path)


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    # Estamos criando um ambiente para o chrome
    # O chrome options permite que o chrome também rode sem
    # mostrar na tela

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # A diferença agora é que criamos um service ao inves
    # de associar diretamente ao chrome

    chrome_service = Service(
        executable_path=chrome_driver_path
    )
    # No caso, instanciamos o service com o patah do chrome driver

    browser = webdriver.Chrome(
        service_args=chrome_service,
        options=chrome_options
    )

    return browser

if __name__ == '__main__':
    browser = make_chrome_browser('--disable-gpu', '--no-sandbox')

    # A partir disso, utilizamos como utilizavamos antes...
    browser.get('htttps://www.google.com')
    sleep(10)
    browser.quit()
