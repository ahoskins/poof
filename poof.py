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
@click.argument('space_name')
def space(space_name):
	space = Space()
	space.add(space_name)


'''
Usage: $ poof add <space-name> <<application-name>>
Effect: add the application to the JSON corresponding to space
'''
@cli.command()
@click.argument('space_name')
@click.argument('application_name')
def add(space_name, application_name):
	the_application = Application()
	the_application.add(application_name, space_name)


'''
Usage: $ poof start <<space-name>>
Effect: parse JSON corresponding to space into a set of bash commands
'''
@cli.command()
@click.argument('space_name')
def start(space_name):
	space = Space()
	space.start(space_name)


'''
Usage: $ poof delete <<space-name> <<application-name>> ... OR ... $ poof delete <<space-name>>
Effect: delete application from space ... OR ... delete entire space 
'''
@cli.command()
@click.argument('space_name')
@click.argument('application_name', required=False)
def delete(space_name, application_name):
	if application_name != None:
		application = Application()
		application.delete(space_name, application_name)
	else:
		the_space = Space()
		the_space.delete(space_name)

		
