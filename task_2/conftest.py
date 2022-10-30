import os
import logging
import pytest
from selenium import webdriver
from selene.support.shared import config
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


def custom_driver(t_browser):
    """ Custom driver """
    logging.debug('custom driver config start')
    if t_browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise ValueError('t_browser does not set')
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    config.timeout = 10
    logging.debug('custom driver config finish')
    return driver


@pytest.fixture(scope='session')
def t_browser(request):
    """  Test browser. Params: [chrome, opera, firefox].  """
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def browser_session(t_browser):
    config.driver = custom_driver(t_browser)
    yield config.driver
    config.driver.quit()


@pytest.fixture()
def rename_file(request, iterate):
    def _rename_file(css_files):
        path = os.getcwd()
        os.rename(f'{path}{PATH_FILES_SITE}/{css_files[iterate]}',
                  f'{path}{PATH_FILES_SITE}/new{css_files[iterate]}')

        def _return_file_name():
            os.rename(f'{path}{PATH_FILES_SITE}/new{css_files[iterate]}',
                      f'{path}{PATH_FILES_SITE}/{css_files[iterate]}')

        request.addfinalizer(_return_file_name)

    return _rename_file
