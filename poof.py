'''
Copyright 2015 Andrew Hoskins

A quick command line tool to open up a setup for an activity
Examples could be: Android development, web dev, music, writing, blogging, etc
'''

import click
import os
import json

from activity import *
from application import *


'''
A command line group...all the below commands stem off this group
'''
@click.group()
def cli():
	pass


'''
Usage: $ poof activity <activity-name>
Effect: create new activity in JSON file
'''
@cli.command()
@click.argument('name')
def activity(name):
	activity = Activity()
	activity.add(name)


'''
Usage: $ poof add <application-name> <<activity-name>>
Effect: add the application to the JSON corresponding to activity
'''
@cli.command()
@click.argument('name')
@click.argument('activity')
def add(name, activity):
	application = Application()
	application.add(name, activity)


'''
Usage: $ poof start <<activity-name>>
Effect: parse JSON corresponding to activity into a set of bash commands
'''
@cli.command()
@click.argument('name')
def start(name):
	activity = Activity()
	activity.start(name)


'''
Usage: $ poof delete <<application-name>> <<activity-name>>
Effect: delete application from activity in the JSON
'''
@cli.command()
@click.argument('name')
@click.argument('activity')
def deletes(name, activity):
	application = Application()
	application.delete(name, activity)


'''
Usage: $ poof delete <<activity-name>>
Effect: delete the entire activty in the JSON
'''
@cli.command()
@click.argument('name')
def delete(name):
	activity = Activity()
	activity.delete(name)

		
