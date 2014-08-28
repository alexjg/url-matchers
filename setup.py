from distutils.core import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("./requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='url-matchers',
    version='0.0.1',
    modules=['url_matchers'],
    install_requires=reqs,
    author="Alex Good",
    author_email="alex@makerlabs.co.uk",
    url="https://github.com/alexjg/url-matchers",
)
