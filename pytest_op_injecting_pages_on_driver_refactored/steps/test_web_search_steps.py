from pytest_bdd import given, when, then, scenarios, parsers
from selenium.webdriver.support import expected_conditions as exp_conditions

scenarios('../features/search.feature')


@given('the user is in the numerade home screen')
def impl(driver):
    driver.get('https://www.numerade.com/')
    driver.wait.until(exp_conditions.visibility_of_element_located(driver.pages.home.mapping.LOGO))


@given(parsers.parse('He fills the search filed with the following word "{word}"'))
def impl(driver, word):
    driver.wait.until(exp_conditions.visibility_of_element_located(driver.pages.home.mapping.INPUT_SEARCH_FIELD)).send_keys(
        word)


@when('He clicks on search button')
def impl(driver):
    driver.wait.until(exp_conditions.visibility_of_element_located(driver.pages.home.mapping.BTN_SEARCH)).click()
