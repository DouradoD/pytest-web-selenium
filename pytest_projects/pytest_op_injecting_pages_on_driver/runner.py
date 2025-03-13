import pytest


def main():
    # https://pytest-html.readthedocs.io/en/latest/installing.html
    # https://docs.pytest.org/en/6.2.x/usage.html
    pytest_commands = ['--tb=auto', '--html', 'report.html', '--self-contained-html']
    pytest.main(pytest_commands)


if __name__ == "__main__":
    main()
