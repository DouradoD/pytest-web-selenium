from selenium.webdriver.common.by import By
from pytest_projects.pytest_op_injecting_pages_on_driver_refactored.factory.page_factory import mappings_wrapper as mapping


@mapping(page='home')
class HomeMappings:
    LOGO = (By.CSS_SELECTOR, '[id="navbar"] img[class="navbar-logo-img"]')
    INPUT_SEARCH_FIELD = (By.CSS_SELECTOR, '[id="navbar"] input[id="search-input"]')
    BTN_SEARCH = (By.CSS_SELECTOR, '[id="navbar"] button[class*="search"]')
