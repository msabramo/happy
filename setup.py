from setuptools import setup, find_packages


setup(
    name="happy",
    version="1.0.0",
    author="Joe Friedl",
    author_email="joe@joefriedl.net",
    url="https://github.com/grampajoe/happy",
    description="Quickly set up and tear down Heroku apps!",
    install_requires=[
        'click',
        'requests'
    ],
    entry_points="""
        [console_scripts]
        happy=happy.cli:cli
    """,
    packages=find_packages(exclude=['tests'])
)
