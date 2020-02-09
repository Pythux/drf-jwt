from setuptools import setup

setup(
    name='drf-jwt',
    version='0.1',
    description='simple jwt handling for django',
    author='Pythux',
    # author_email='',
    packages=['drf_jwt'],  # same as name, change '⁻' to '_'
    # install_requires=[],  # external packages as dependencies
)

# install in dev mode:
# pip install --editable .
