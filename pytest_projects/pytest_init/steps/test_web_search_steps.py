from pytest_bdd import given, when, then, scenarios, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_conditions

scenarios('../features/search.feature')

LOGO = (By.CSS_SELECTOR, '[id="navbar"] img[class="navbar-logo-img"]')
INPUT_SEARCH_FIELD = (By.XPATH, '//input[@id="search-text"]')
BTN_SEARCH = (By.CSS_SELECTOR, 'button[id="search-lens-btn"]')
TXT_SEARCH_QUERY = (By.ID, 'search-query-label')


@given('the user is in the numerade home screen')
def impl(driver):
    driver.get('https://www.numerade.com/')
    driver.wait.until(exp_conditions.visibility_of_element_located(LOGO))


@given(parsers.parse('He fills the search filed with the following word "{word}"'))
def impl(driver, word):
    driver.wait.until(exp_conditions.visibility_of_element_located(INPUT_SEARCH_FIELD)).send_keys(
        word)


@when('He clicks on search button')
def impl(driver):
    driver.wait.until(exp_conditions.visibility_of_element_located(BTN_SEARCH)).click()

@then('the result screen should be displayed')
def impl(driver):
  driver.wait.until(exp_conditions.visibility_of_element_located(TXT_SEARCH_QUERY))
