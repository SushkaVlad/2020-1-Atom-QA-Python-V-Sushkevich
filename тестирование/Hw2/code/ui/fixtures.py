import time

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


from ui.pages.auth_problem_page import AuthProblemPage
from ui.pages.base_page import BasePage
from ui.pages.create_company_page import CreateCompanyPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.segments_page import SegmentsPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def auth_problem_page(driver):
    return AuthProblemPage(driver=driver)


@pytest.fixture
def create_company_page(driver):
    return CreateCompanyPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)


@pytest.fixture
def correct_auth_data():
    return {'login': 'vladislav2908@gmail.com', 'password': 'technoatom2020'}


@pytest.fixture
def incorrect_auth_data():
    return {'login': 'vladislav2907@gmail.com', 'password': 'technoatom2021'}


@pytest.fixture
def log_to_main_page(driver, correct_auth_data):
    lg_page = LoginPage(driver)
    lg_page.click(lg_page.locators.ENTER_BUTTON)
    lg_page.fill_field(lg_page.locators.INPUT_LOGIN, correct_auth_data['login'])
    lg_page.fill_field(lg_page.locators.INPUT_PASSWORD, correct_auth_data['password'])
    lg_page.find(lg_page.locators.GO_TO_MAIN_PAGE_BUTTON).click()
    mn_page = MainPage(driver)
    yield mn_page
    mn_page.click(mn_page.locators.USER_BUTTON)
    time.sleep(0.5)
    mn_page.click(mn_page.locators.LOG_OUT)


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install(),
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )

        # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub/',
        #                         options=options,
        #                          desired_capabilities={'acceptInsecureCerts': True}
        #                          )

    else:
        raise UsupportedBrowserException(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
