import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True, scope="session")
def browser_settings():

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()