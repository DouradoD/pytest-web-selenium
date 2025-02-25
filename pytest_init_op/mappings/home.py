from selenium.webdriver.common.by import By


class HomeMappings:
    LOGO = (By.CSS_SELECTOR, '[id="navbar"] img[class="navbar-logo-img"]')
    INPUT_SEARCH_FIELD = (By.XPATH, '//input[@id="search-text"]')
    BTN_SEARCH = (By.CSS_SELECTOR, 'button[id="search-lens-btn"]')
    TXT_SEARCH_QUERY = (By.ID, 'search-query-label')
