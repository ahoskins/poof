from setuptools import setup, find_packages

setup(
    name='poof',
    version='0.1',
    packages=['poof'],
    install_requires=[
        'Click', 'fuzzywuzzy',
    ],
    entry_points='''
        [console_scripts]
        poof=poof.poof:cli
    ''',
)