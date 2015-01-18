import os
import json

file_path = os.environ['HOME'] + '/.poof'


'''
File setup

If $HOME/.poof does not exist, create it
Otherwise, assume it's not empty and read in the contents

In either case, store a file handle
'''
if '.poof' not in os.listdir(os.environ['HOME']):
	open(file_path, 'w').close()
else:
	all_data = json.load(open(file_path, 'r'))

json_file = open(file_path, 'r+')


'''
Invoked after: $ poof activity <new-activity>

Store the JSON in $HOME/.poof
Either the file exists or it doesn't...respond accordingly
'''
def newActivity(name):
	home_files = os.listdir(os.environ['HOME'])

	if os.stat("/Users/Andrew/.poof").st_size != 0:
		# Read in the JSON, and append to the de-serialized object
		all_data["activities"].append({"sources": [], "activity": name})

		# Empty the file
		delete(json_file)

		# Dump the object back to the file
		json.dump(all_data, json_file, indent=4)

	else:
		json.dump({"activities": [{"sources": [], "activity": name}]}, json_file, indent=4)

	json_file.close()


'''
Used to clear the file contents
'''
def delete(file):
	file.seek(0)
	file.truncate()


'''
Invoked after: $ poof add <application-name> <<activity>>

Adds application to activity in JSON
'''
def addApplication(application, activity):
	if not isAllowed(activity):
		return

	for entry in all_data["activities"]:
		if entry["activity"] == activity:
			entry["sources"].append("/Applications/" + application)

	delete(json_file)

	json.dump(all_data, json_file, indent=4)

	json_file.close()


'''
Called by addApplication to verify if the activity has been created first
'''
def isAllowed(activity):
	# Does the file even exist?
	if '.poof' not in os.listdir(os.environ['HOME']):
		print "Hey you! Add the activity first."
		return False

	# Does the file contain that activity?
	for entry in all_data["activities"]:
		if entry["activity"] == activity:
			return True

	# It didn't contain the activity
	print "Hey you! Add the activity first."
	return False


'''
Invoked after: $ poof start <<activity>>

System open command the files under the activity in the JSON file
'''
def startActivity(activity):
	# Does the activity exists?
	if not isAllowed(activity):
		return

	for entry in all_data["activities"]:
		if entry["activity"] == activity:
			for source in entry["sources"]:
				os.system("open " + source + ".app")


	json_file.close()


def deleteApplication(application, activity):
	if not isAllowed(activity):
		return

	index = 0;
	for entry in all_data['activities']:
		if entry['activity'] == activity:
			for source in entry['sources']:
				if source == ('/Applications/' + application):
					print "should delete"
					del entry['sources'][index]
				index = index + 1

	delete(json_file)
	json.dump(all_data, json_file, indent=4)
	json_file.close()

def deleteActivity(activity):
	if not isAllowed(activity):
		return

	index = 0;
	for entry in all_data['activities']:
		if entry['activity'] == activity:
			del all_data['activities'][index]
		index = index + 1

	delete(json_file)
	json.dump(all_data, json_file, indent=4)
	json_file.close()







