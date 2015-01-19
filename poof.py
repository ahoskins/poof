'''
Copyright 2015 Andrew Hoskins

A quick command line tool to open up a setup for an space
Examples could be: Android development, web dev, music, writing, blogging, etc
'''

import click
import os
import json

from space import *
from application import *


'''
A command line group...all the below commands stem off this group
'''
@click.group()
def cli():
	pass


'''
Usage: $ poof space <space-name>
Effect: create new space in JSON file
'''
@cli.command()
@click.argument('name')
def space(name):
	space = Space()
	space.add(name)


'''
Usage: $ poof add <application-name> <<space-name>>
Effect: add the application to the JSON corresponding to space
'''
@cli.command()
@click.argument('name')
@click.argument('space')
def add(name, space):
	application = Application()
	application.add(name, space)


'''
Usage: $ poof start <<space-name>>
Effect: parse JSON corresponding to space into a set of bash commands
'''
@cli.command()
@click.argument('name')
def start(name):
	space = Space()
	space.start(name)


'''
Usage: $ poof delete <<space-name> <<application-name>> ... OR ... $ poof delete <<space-name>>
Effect: delete application from space ... OR ... delete entire space 
'''
@cli.command()
@click.argument('space')
@click.argument('app', required=False)
def delete(space, app):
	if app != None:
		application = Application()
		application.delete(app, space)
	else:
		the_space = Space()
		the_space.delete(space)

		
