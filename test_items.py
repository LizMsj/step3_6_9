from selenium import webdriver
import pytest


def test_check_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary')\
    assert button, "Нет кнопки 'добавить в корзину'"
