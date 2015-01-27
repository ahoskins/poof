from storage import *
from validation import *

'''
Class responsible for controlling the creation of applications
'''

class Application:
	
	'''
	Capture an instance of the Storage class
	'''
	def __init__(self):
		self.storage = Storage()


	'''
	Add an application to the space in the JSON

	@returns: nothing
	'''
	def add(self, name, space):
		name = name + '.app'

		validate = Validation()
		if validate.matchAgainstDirectory(name):
			self.storage.addApplication(name, space)
		
		fuzzy_result = validate.fuzzyAgainstDirectory(name)
		if fuzzy_result != None:
			self.storage.addApplication(fuzzy_result, space)


	'''
	Delete an application from an space in the JSON

	@returns: nothing
	'''
	def delete(self, space, name):
		name = name + '.app'

		self.storage.deleteApplication(space, name)