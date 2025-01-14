from setuptools import setup

setup(
    name="omasjl",
    version="0.1.0",
    author="Orso Meneghini",
    packages=["omasjl"],
    install_requires=[
        'julia',
    ],
    package_data = {'omasjl': ['*.py', 'version']},
)
