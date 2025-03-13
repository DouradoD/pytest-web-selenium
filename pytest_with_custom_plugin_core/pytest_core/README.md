# Core Plugin for Pytest
The Core Plugin is a custom pytest plugin designed to simplify and enhance test automation workflows. It provides essential fixtures, configurations, and utilities for writing robust and maintainable tests, particularly for web automation using Selenium.

## Features
Pre-configured Selenium WebDriver Fixture: Automatically manages the lifecycle of a WebDriver instance.

Customizable Options: Easily configure browser options and settings. WIP

Session-Scoped Fixtures: Ensures efficient resource management for long-running tests.

Integration with pytest-bdd: Supports Behavior-Driven Development (BDD) testing.

HTML Reporting: Generates detailed HTML test reports using pytest-html.

## Installation


To install the core plugin, use pip:

``` bash
   pip install .    
```
If you're working in a development environment, you can install it in editable mode:

``` bash
   pip install -e .    
```

### Usage
1. Basic Usage
The core plugin provides a driver fixture that can be used in your tests. Here's an example:

# tests/test_example.py
``` python
def test_web_search(driver):
    driver.get("https://www.example.com")
    assert "Example" in driver.title

```

2. Customizing Browser Options, check of Custom options: by:

Ex:
```
   pytest --help
   
   ...
   Custom options:
  --browser=BROWSER     Specify the browser name: Chrome, Edge, Firefox or Opera, by default is Chrome
  --webdriver_manager_enabled=WEBDRIVER_MANAGER_ENABLED
                        Specify True to use the webdriver_manager, by default is False
  --driver_path=DRIVER_PATH
                        Specify the driver path, C:./../chromedriver.exe, by default is None
  --headless=HEADLESS   Specify the headless value, by default is False

```


3. Using with pytest-bdd
The core plugin integrates seamlessly with pytest-bdd. Here's an example:


# tests/test_bdd.py
from pytest_bdd import scenarios, given, when, then

```python
from pytest_bdd import scenarios, given, when, then

scenarios("features/web_search.feature")

@given("I am on the homepage")
def homepage(driver):
    driver.get("https://www.example.com")

@then("the title should contain 'Example'")
def check_title(driver):
    assert "Example" in driver.title
```


4. Generating HTML Reports
To generate an HTML report, run pytest with the --html option:

```
pytest --html=report.html
```
## setup.py key point
Entry Points
The core plugin is automatically discovered by pytest via the following entry point in setup.py:

```python
entry_points={
    "pytest11": [
        "core = core.custom_pytest_setup",
    ]
}

```
##  Fixtures
| Fixture                | Scope      | Description |
|------------------------|------------|-------------|
| driver                 | Session    |Provides a WebDriver instance for browser automation.|
| browser_options (#WIP) | Function   |Allows customization of browser options.|
```python
import pytest
from pytest_core.session_info import SessionInfo
from pytest_core.custom_driver import CustomerDriver

@pytest.fixture(scope='session')
def driver(request):
    session_info = SessionInfo(request_config=request.config)
    custom_driver = CustomerDriver(session_info=session_info)
    driver = custom_driver.driver(timeout=15)
    driver.maximize_window()
    print('Finished to create the driver!')

    print('The pytest_with_core_plugin are going to run ....')
    yield driver

    print('Finishing the Driver/Tests')
    driver.quit()
```

# Contributing
We welcome contributions! If you'd like to contribute to the core plugin, follow these steps:

## Fork the repository.

Create a new branch for your feature or bugfix.

Write tests for your changes.

Submit a pull request.

### License
WIP

### Support
For questions, issues, or feature requests, please open an issue on the GitHub repository.

### Acknowledgments
- Selenium: For browser automation. 
- pytest: For the testing framework. 
- pytest-bdd: For Behavior-Driven Development support. 
- pytest-html: For HTML reporting.

### Changelog
v0.1.0 (Initial Release)
- Added driver fixture for WebDriver management. 
- Integrated with pytest-bdd and pytest-html.