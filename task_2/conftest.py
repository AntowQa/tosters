import os
import logging
import pytest
from selenium import webdriver
from selene.support.shared import config
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from helpers.base_helper import get_css_files
from settings import PATH_FILES_SITE


def pytest_addoption(parser):
    """ Pytest option variables"""
    parser.addoption('--browser',
                     help=u'Test browser',
                     choices=['chrome'],
                     default='chrome')

    parser.addoption('--headless',
                     help=u'Headless mode',
                     choices=['y', 'n'],
                     default='n')


def custom_driver(t_browser, t_headless):
    """ Custom driver """
    logging.debug('custom driver config start')
    if t_browser == 'chrome':
        if t_headless == 'y':
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=headless_chrome_options())
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise ValueError('t_browser does not set')
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    config.timeout = 10
    logging.debug('custom driver config finish')
    return driver


def headless_chrome_options():
    """ Custom chrome options """
    logging.info('set chromedriver options start')
    chrome_options = Options()
    chrome_options.set_capability("pageLoadStrategy", "eager")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--enable-automation")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-setuid-sandbox")
    logging.info('set chromedriver options finish')
    return chrome_options


@pytest.fixture(scope='session')
def t_browser(request):
    """  Test browser. Params: [chrome, opera, firefox].  """
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def t_headless(request):
    return request.config.getoption('--headless')


@pytest.fixture(scope='session')
def browser_session(t_browser, t_headless):
    config.driver = custom_driver(t_browser, t_headless)
    yield config.driver
    config.driver.quit()


@pytest.fixture()
def rename_file(request, iterate):
    css_files = get_css_files()
    path = os.getcwd()
    os.rename(f'{path}{PATH_FILES_SITE}/{css_files[iterate]}', f'{path}{PATH_FILES_SITE}/new{css_files[iterate]}')

    def return_file_name():
        os.rename(f'{path}{PATH_FILES_SITE}/new{css_files[iterate]}', f'{path}{PATH_FILES_SITE}/{css_files[iterate]}')
    request.addfinalizer(return_file_name)
