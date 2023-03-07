from setuptools import setup, find_packages

setup(
    name='learning_pytest',
    extras_require = dict(test=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"":"src"},
)