import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.wait = WebDriverWait(driver=driver, timeout=15)
    return driver


def pytest_bdd_before_scenario(request):
    driver = request.getfixturevalue('driver')
    driver.maximize_window()


def pytest_bdd_after_scenario(request):
    driver = request.getfixturevalue('driver')
    driver.quit()
