import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language: es, ru and else")
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose browser: Firefox or Chrome")


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    user_browser = request.config.getoption('browser_name')
    if user_browser == 'Chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif user_browser == 'Firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    browser.quit()
