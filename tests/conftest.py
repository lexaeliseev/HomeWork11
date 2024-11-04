import pytest
from selene import browser


@pytest.fixture(autouse=True, scope="session")
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://demoqa.com"
    yield
    browser.quit()
