import os
import json

'''
Invoked after: $ poof activity <new-activity>

Store the JSON in $HOME/.poof
Either the file exists or it doesn't...respond accordingly
'''
def newActivity(name):
	file_path = os.environ['HOME'] + '/.poof'
	home_files = os.listdir(os.environ['HOME'])

	if '.poof' in home_files:
		# Read in the JSON, and append to the de-serialized object
		json_file_r = open(file_path, 'r')
		all_data = json.load(json_file_r)
		all_data["activities"].append({"sources": [], "activity": name})

		# Dump the object back to the file
		json_file_w = open(file_path, 'w')
		json.dump(all_data, json_file_w, indent=4)

	else:
		json_file = open(file_path, 'w')
		json.dump({"activities": [{"sources": [], "activity": name}]}, json_file, indent=4)

'''
Invoked after: $ poof add <application-name> <<activity>>
'''
def addApplication(application, activity):
	file_path = os.environ['HOME'] + '/.poof'

	if not isAllowed(activity):
		return

	json_file_r = open(file_path, 'r')
	all_data = json.load(json_file_r)

	for entry in all_data["activities"]:
		if entry["activity"] == activity:
			entry["sources"].append("/Applications/" + application)

	json_file_w = open(file_path, 'w')
	json.dump(all_data, json_file_w, indent=4)

'''
Called by addApplication to verify if the activity has been created first
'''
def isAllowed(activity):
	# Does the file even exist?
	if '.poof' not in os.listdir(os.environ['HOME']):
		print "Hey you! Add an activity first."
		return False

	# Does the file contain that activity?
	json_file_r = open(os.environ['HOME'] + '/.poof', 'r')
	all_data = json.load(json_file_r)
	for entry in all_data["activities"]:
		if entry["activity"] == activity:
			return True

	# It didn't contain the activity
	print "Hey you! Add an activity first."
	return False





