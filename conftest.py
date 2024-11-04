import pytest
from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def open_browser():
    browser.config.base_url = "https://demoqa.com"
    yield
    browser.quit()


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "124.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))

    yield browser

    browser.quit()
