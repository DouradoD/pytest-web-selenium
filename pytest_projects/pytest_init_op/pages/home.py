from pytest_projects.pytest_init_op.mappings.home import HomeMappings


def home_page():
    return Home()


class Home:
    def __init__(self):
        self._mapping = HomeMappings()

    @property
    def mapping(self):
        return self._mapping
