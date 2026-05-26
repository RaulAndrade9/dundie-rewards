from setuptools import setup, find_packages

setup(
    name = "dundie",
    version = "0.1.0",
    description = "Rewards points system for Dunder Mifflin",
    author = "Raul Andrade",
    packages = find_packages(),
    name="dundie",
    version="0.1.0",
    description="Rewards points system for Dunder Mifflin",
    author="Raul Andrade",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie=dundie.__main__:main"
        ]
    }
)
