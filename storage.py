import os
import json

'''
Class responsible for touching the JSON file.  It is the only entity that modifies the underlying JSON.

It's called from the activity and application class's.
'''

class Storage:

	'''
	Upon creation of object: initialize the file (if not already done), and set up file and data handles
	'''
	def __init__(self):
		self.file_path = os.environ['HOME'] + '/.poof'

		# If $HOME/.poof doesn't exists, create and initialize it with an empty "activities" array
		if '.poof' not in os.listdir(os.environ['HOME']):
			new_file = open(self.file_path, 'w')
			json.dump({"activities": []}, new_file, indent=4)
			new_file.close()

		# Create file handle and JSON data object for read and write
		self.json_file = open(self.file_path, 'r+')
		self.all_data = json.load(self.json_file)


	'''
	Deletes the contents of the JSON file_path

	Used as part of the update-write cycle...prevents data from being duplicated

	@returns: nothing
	'''
	def delete(self):
		self.json_file.seek(0)
		self.json_file.truncate()


	'''
	Copy self.all_data into self.json_file with pretty formatting <3

	@returns: nothing
	'''
	def dumpData(self):
		json.dump(self.all_data, self.json_file, indent=4)


	'''
	Add activity object to JSON file

	@returns: nothing
	'''
	def addActivity(self, activity):
		self.all_data['activities'].append(activity)
		self.delete()
		self.dumpData()
		print "Activity added successfully."
		self.json_file.close()


	'''
	Get a specified activity object from JSON

	@returns: activity object or -1
	'''
	def getActivity(self, activity):
		for activity_obj in self.all_data['activities']:
			if activity_obj['activity'] == activity:
				return activity_obj

		# Activity didn't exist
		return -1


	'''
	Delete a specified activity object from JSON

	@returns: nothing 
	'''
	def deleteActivity(self, activity):
		index = 0
		for activity_obj in self.all_data['activities']:
			if activity_obj['activity'] == activity:
				del self.all_data['activities'][index]
				self.delete()
				self.dumpData()
				self.json_file.close()
				print 'Activity ' + activity +  ' deleted.'
				return
			index = index + 1

		# Activity didn't exist
		print activity + ' does not exist.'


	'''
	Add an application to the specified activity array in JSON

	@returns: nothing
	'''
	def addApplication(self, application, activity):
		for activity_obj in self.all_data['activities']:
			if activity_obj['activity'] == activity:
				activity_obj['sources'].append('/Applications/' + application)
				self.delete()
				self.dumpData()
				print 'Application added successfully.'
				self.json_file.close()
				return

		# Activity didn't exist
		print 'The activity you ask for does not exist.'


	'''
	Delete specified application from specified activity in JSON

	@returns: nothing
	'''
	def deleteApplication(self, application, activity):
		index = 0
		for activity_obj in self.all_data['activities']:
			if activity_obj['activity'] == activity:
				for source in activity_obj['sources']:
					if source == ('/Applications/' + application):
						del activity_obj['sources'][index]
						self.delete()
						self.dumpData()
						print 'Application ' + application + ' deleted.'
						self.json_file.close()
						return
					index = index + 1

		# Activity didn't exist
		print 'The activity you ask for does not exist.'


