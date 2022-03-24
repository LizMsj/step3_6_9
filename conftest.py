import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or es")

@pytest.fixture.language(scope="function")
def language():
    pass

@pytest.fixture.browser(scope="function", )
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
