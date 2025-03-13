from selenium.webdriver.common.by import By


class HomeMappings:
    LOGO = (By.CSS_SELECTOR, '[id="navbar"] img[class="navbar-logo-img"]')
    INPUT_SEARCH_FIELD = (By.CSS_SELECTOR, '[id="navbar"] input[id="search-input"]')
    BTN_SEARCH = (By.CSS_SELECTOR, '[id="navbar"] button[class*="search"]')
