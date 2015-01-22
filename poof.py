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
import subprocess


'''
A command line group...all the below commands stem off this group
'''
@click.group()
def cli():
	pass

'''
An alias for --help because sometimes people hate typing in those extra dashes
'''
@cli.command()
def help():
	"""The wonderful help page"""
	subprocess.call(['poof', '--help'])
	pass


'''
Usage: $ poof space <space-name>
Effect: create new space in JSON file
'''
@cli.command(options_metavar='')
@click.argument('space_name', metavar='<space-name>')
def space(space_name):
	"""Add a label for an application group"""
	space = Space()
	space.add(space_name)


'''
Usage: $ poof add <space-name> <<application-name>>
Effect: add the application to the JSON corresponding to space
'''
@cli.command(options_metavar='')
@click.argument('space_name', metavar='<space-name>')
@click.argument('application_name', metavar='<application-name>')
def add(space_name, application_name):
	"""Add an application to a space"""
	the_application = Application()
	the_application.add(application_name, space_name)


'''
Usage: $ poof start <<space-name>>
Effect: parse JSON corresponding to space into a set of bash commands
'''
@cli.command(options_metavar='')
@click.argument('space_name', metavar='<space-name>')
def start(space_name):
	"""Open all applications added to the space"""
	space = Space()
	space.start(space_name)


'''
Usage: $ poof delete <<space-name> <<application-name>> ... OR ... $ poof delete <<space-name>>
Effect: delete application from space ... OR ... delete entire space 
'''
@cli.command(options_metavar='')
@click.argument('space_name', metavar='<space-name>')
@click.argument('application_name', required=False, metavar='<application-name>')
def delete(space_name, application_name):
	"""Deletes the ENTIRE space if application name NOT given.  Deletes the SINGLE application from the space if name IS given."""
	if application_name != None:
		application = Application()
		application.delete(space_name, application_name)
	else:
		the_space = Space()
		the_space.delete(space_name)

		
