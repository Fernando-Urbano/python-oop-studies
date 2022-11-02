"""
Selenium
13/02/2022

Automatizar tarefas.
Temos que acessar o pypi.
Dentro do pypi procuramos selenium e dentro do selenium procuramos pelo driver do
navegador que eu quero utilizar. O drive é uma especie de interface que possibilita
mandar comandos do script para o navegador.
Tenho que baixar um driver com a versão do meu navegador.

No caso, vamos utilizar do Chrome.
No chrome, baixamos a versão para windows.
É importante colocar o chrome driver no mesmo lugar de onde está o nosso projeto.

"""
from selenium import webdriver
from time import sleep

import pathlib

scriptDirectory = pathlib.Path().absolute()


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        # Se o chromedriver estivesse em outro caminho, seria importante
        # colocar o caminho completo
        self.options = webdriver.ChromeOptions()
        # Vamos dizer que o perfil que foi criado será salvo dentro do meu diretório
        self.options.add_argument(f"user-data-dir={scriptDirectory}\\Perfil")
        # Vamos usar a pasta Perfil
        # Abaixo, estamos colocando um atributo que é o próprio Chrome
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

        # Isso é padrão. O que será utilizado depois é que vai dirvergir de site para
        # site

    def clicar_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            # Buscamos o texto pelo que está escrito nele
            btn_sign_in.click()
        except Exception as error:
            print('Erro: ', error)

    def realizar_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            input_login.send_keys('fernando.rocha.urbano@gmail.com')
            input_password.send_keys('Frcu@7082')
            sleep(3)
            btn_login = self.chrome.find_element_by_name('commit')
            # O name não necessariamente será o que está escrito.
            # Temos que clicar em ispecionar para verificar.
            # Por exemplo, o Sign in na verdade é commit.
            btn_login.click()
        except Exception as error:
            print('Erro ao fazer login: ', error)

    def clicar_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details'
            )
            perfil.click()
            # No caso, a ideia é clicarmos no perfil e iremos fazer isso clicando no perfil
            # com inspecionar. Após, vamos na parte de html do perfil e clicaremos em copy.
            # Após o copy, é necessário especificar que estamos falando de copy selector.
            # O seletor é vantajoso quando não temos um id
        except Exception as error:
            print(error)

    def clicar_logoff(self):
        try:
            logoff = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button'
            )
            logoff.click()
        except Exception as error:
            print(error)

    def verificar_usuario(self):
        try:
            try:
                profile_link = self.chrome.find_element_by_css_selector(
                   'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > div.header-nav-current-user.css-truncate > a'
                )
            except:
                try:
                    profile_link = self.chrome.find_element_by_class_name(
                        'no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block'
                    )
                except:
                    profile_link = self.chrome.find_element_by_class_name(
                        'user-profile-link'
                    )
            profile_link_html = profile_link.get_attribute('innerHTML')
            print(profile_link_html)
        except Exception as error:
            print(error)

    def acessar(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://github.com/')
    chrome.clicar_sign_in()
    chrome.realizar_login()
    chrome.clicar_perfil()
    chrome.verificar_usuario()
    sleep(3)
    chrome.clicar_logoff()
    sleep(3)
    chrome.sair()
