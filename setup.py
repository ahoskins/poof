from setuptools import setup

setup(
    name='poof',
    version='0.1',
    py_modules=['poof', 'storage', 'space'],
    install_requires=[
        'Click', 'fuzzywuzzy',
    ],
    entry_points='''
        [console_scripts]
        poof=poof:cli
        ''',
    )