import json
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from steps.login_steps import LoginSteps
from selene.api import browser


DEFAULT_WAIT_TIME = 10
CONFIG_PATH = 'C:/Users/Lidiia/PycharmProjects/tests/config_prod.json'


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope="session")
def browser(config_wait_time):
    browser_name = config['browser']
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    elif browser_name == "ff":
        driver = webdriver.Firefox(service=Service("geckodriver"), options=Options())
    elif browser_name == "ie":
        driver = webdriver.Ie(service=Service('IEDriverServer'))
    else:
        raise Exception(f'"{browser_name}" is not a supported browser')
    browser.driver = driver
    browser.driver.implicitly_wait(config_wait_time)
    yield browser
    browser.quit_driver()


@pytest.fixture(scope="session")
def setup_login(config):
    login_page = LoginSteps()
    login_page.login(config['url'], config['org'], config['username'], config['password'])
    login_page.browser.driver.maximize_window()


@pytest.fixture(scope="session")
def receive_access_token(config):
    return requests.post(
        config['ciam'],
        headers={"Accept": "application/json",
                 "Content-Type": "application/json",
                 "x-org-id": config['org'],
                 "Authorization": config['basic_login_token']},
        json={"username": config['username'],
              "password": config['password']}).json()["auth"]["access_token"]
