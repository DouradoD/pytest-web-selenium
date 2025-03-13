import pytest
import sys


def get_args():
    args = sys.argv
    args.pop(0)
    return args


def main():
    additional_args = get_args()
    # https://pytest-html.readthedocs.io/en/latest/installing.html
    # https://docs.pytest.org/en/6.2.x/usage.html
    pytest_commands = ['--tb=auto', '--html', 'report.html', '--self-contained-html']
    pytest_commands = pytest_commands + additional_args
    pytest.main(pytest_commands)


if __name__ == "__main__":
    main()
