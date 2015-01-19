import os
import json

'''
Class responsible for touching the JSON file.  It is the only entity that modifies the underlying JSON.

It's called from the space and application class's.
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
	Add space object to JSON file

	@returns: nothing
	'''
	def addSpace(self, space):
		self.all_data['activities'].append(space)
		self.delete()
		self.dumpData()
		print "space added successfully."
		self.json_file.close()


	'''
	Get a specified space object from JSON

	@returns: space object or -1
	'''
	def getSpace(self, space):
		for space_obj in self.all_data['activities']:
			if space_obj['space'] == space:
				return space_obj

		# space didn't exist
		return -1


	'''
	Delete a specified space object from JSON

	@returns: nothing 
	'''
	def deleteSpace(self, space):
		index = 0
		for space_obj in self.all_data['activities']:
			if space_obj['space'] == space:
				del self.all_data['activities'][index]
				self.delete()
				self.dumpData()
				self.json_file.close()
				print 'space ' + space +  ' deleted.'
				return
			index = index + 1

		# space didn't exist
		print space + ' does not exist.'


	'''
	Add an application to the specified space array in JSON

	@returns: nothing
	'''
	def addApplication(self, application, space):
		for space_obj in self.all_data['activities']:
			if space_obj['space'] == space:
				space_obj['sources'].append('/Applications/' + application)
				self.delete()
				self.dumpData()
				print 'Application added successfully.'
				self.json_file.close()
				return

		# space didn't exist
		print 'The space you ask for does not exist.'


	'''
	Delete specified application from specified space in JSON

	@returns: nothing
	'''
	def deleteApplication(self, space, application):
		index = 0
		for space_obj in self.all_data['activities']:
			if space_obj['space'] == space:
				for source in space_obj['sources']:
					if source == ('/Applications/' + application):
						del space_obj['sources'][index]
						self.delete()
						self.dumpData()
						print 'Application ' + application + ' deleted.'
						self.json_file.close()
						return
					index = index + 1

		# space didn't exist
		print 'The space you ask for does not exist.'


