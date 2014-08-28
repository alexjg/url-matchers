from distutils.core import setup
from os import path
from pip.req import parse_requirements

requirements_location = path.join(path.dirname(__file__), "requirements.txt")
install_reqs = parse_requirements(requirements_location)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='url-matchers',
    description="Url matchers for PyHamcrest",
    version='0.0.1',
    modules=['url_matchers'],
    install_requires=reqs,
    author="Alex Good",
    author_email="alex@makerlabs.co.uk",
    url="https://github.com/alexjg/url-matchers",
)
