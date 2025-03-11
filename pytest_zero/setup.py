from setuptools import setup
from setuptools.config.expand import entry_points

setup(
    name="pytest_core",
    version="0.1",
    entry_points={
        "pytest11":[
        "core = pytest_core.pre_setup_custom_plugin"
    ]
}
)