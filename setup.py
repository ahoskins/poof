from setuptools import setup

setup(
	name='poof',
	version='0.1',
	py_modules=['poof'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		poof=poof:cli
		''',
	)