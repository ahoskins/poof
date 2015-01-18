'''
Copyright 2015 Andrew Hoskins

A quick command line tool to open up a setup for an activity
Examples could be: Android development, web dev, music, writing, blogging, etc
'''

import click
import os
import json
from data import *


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
	newActivity(name)

'''
Usage: $ poof add <application-name> <<activity-name>>
Effect: add the application to the JSON corresponding to activity
'''
@cli.command()
@click.argument('application')
@click.argument('activity')
def add(application, activity):
	addApplication(application, activity)

'''
Usage: $ poof start <<activity-name>>
Effect: parse JSON corresponding to activity into a set of bash commands
'''
@cli.command()
@click.argument('activity')
def start(activity):
	startActivity(activity)

		




		

		


