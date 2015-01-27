from distutils.core import setup

setup(
	name='poof',
	author='Andrew Hoskins',
	auther_email='arh.hoskins@gmail.com'
	version = '0.1',
	keywords= ['workspace', 'command-line']
	description='A command line workspace manager for Mac OS X',
	py_modules=['poof', 'storage', 'space'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		poof=poof:cli
		''',
	)