from setuptools import setup, find_packages
from importlib import import_module
from helper_setup import read_readme, activate_cmd_publish


#################################################################


description = 'simple JWT handling for django REST Framework'
url = "https://github.com/Pythux/drf-jwt"
install_requires = ['PyJWT>=1.5.2,<2.0.0']
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP',
]

#################################################################

activate_cmd_publish()  # can do python setup.py publish
__init__ = import_module(find_packages()[0])
setup(
    name=__init__.__title__,
    version=__init__.__version__,
    author=__init__.__author__,
    # author_email='',
    description=description,
    long_description=read_readme(),  # Get the README file, can be .md, .rst, ...
    long_description_content_type="text/markdown",
    url=url,
    packages=find_packages(),  # same as name, change '⁻' to '_'
    classifiers=classifiers,
    install_requires=install_requires,  # external packages as dependencies,
    python_requires='>=3.6',
)

# install in dev mode:
# pip install --editable .
