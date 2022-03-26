from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_check_button_on_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_elements(By.CSS_SELECTOR, '.btn-primary')
    sleep(5)
    assert button, 'basket button not found'
