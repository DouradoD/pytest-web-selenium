from pytest_projects.pytest_op_injecting_pages_on_driver.mappings.home import HomeMappings
from pytest_projects.pytest_op_injecting_pages_on_driver.factory.page_factory import page_wrapper as page


def home_page():
    return Home()


@page(name='home')
class Home:
    def __init__(self):
        self._mapping = HomeMappings()

    @property
    def mapping(self):
        return self._mapping
