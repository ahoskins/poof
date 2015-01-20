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
		validate = Validation()
		if validate.checkMatch(name):
			self.storage.addApplication(name, space)


	'''
	Delete an application from an space in the JSON

	@returns: nothing
	'''
	def delete(self, name, space):
		self.storage.deleteApplication(name, space)