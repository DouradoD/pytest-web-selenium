import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.wait = WebDriverWait(driver=driver, timeout=15)
    driver.maximize_window()
    print('Finished to create the driver!')

    print('The tests are going to run ....')
    yield driver

    print('Finishing the Driver/Tests')
    driver.quit()
