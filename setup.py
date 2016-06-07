from setuptools import setup
from os import path
from pip.req import parse_requirements

setup(
    name='url-matchers',
    description="Url matchers for PyHamcrest",
    version='0.0.4',
    py_modules=['url_matchers'],
    install_requires = [
        "PyHamcrest>=1.8.0",
        "six>=1.7.3",
    ],
    author="Alex Good",
    author_email="alex@makerlabs.co.uk",
    url="https://github.com/alexjg/url-matchers",
)
