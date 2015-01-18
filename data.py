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
		all_data["activities"].append({name: []})

		# Dump the object back to the file
		json_file_w = open(file_path, 'w')
		json.dump(all_data, json_file_w, indent=4)

	else:
		json_file = open(file_path, 'w')
		json.dump({"activities": [{name: []}]}, json_file, indent=4)