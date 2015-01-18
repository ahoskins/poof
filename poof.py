'''
Copyright 2015 Andrew Hoskins

A quick command line tool to open up a setup for an activity
Examples could be: Android development, web dev, music, writing, blogging, etc
'''

import click
import os
import json


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
	click.echo('Hello %s' % name)
	# add to activity to a JSON file called .poof
	newActivity(name)

'''
Usage: $ poof add <application-name> <<activity-name>>
Effect: add the application to the JSON corresponding to activity
'''
@cli.command()
@click.argument('application')
@click.argument('activity')
def add(application, activity):
	click.echo('%s' % application)
	click.echo('%s' % activity)

'''
Usage: $ poof start <<activity-name>>
Effect: parse JSON corresponding to activity into a set of bash commands
'''
@cli.command()
@click.argument('activity')
def start(activity):
	click.echo('%s' % activity)


def newActivity(name):
	# two cases, file exists or it doesn't
	home_files = os.listdir(os.environ['HOME'])
	if '.poof' in home_files:
		print "its there"
		json_file_r = open(os.environ['HOME'] + '/.poof', 'r')

		# load the file
		all_data = json.load(json_file_r)

		# append to this object
		all_data.append({'activity': name})

		json_file_w = open(os.environ['HOME'] + '/.poof', 'w')

		# dump the data back to the file
		json.dump(all_data, json_file_w)
	else:
		print "not there"

		json_file = open(os.environ['HOME'] + '/.poof', 'w')
		data = {'activity': name}
		json.dump([data], json_file)




		

		


