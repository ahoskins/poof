from storage import *

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
	Add an application to the activity in the JSON

	@returns: nothing
	'''
	def add(self, name, activity):
		self.storage.addApplication(name, activity)


	'''
	Delete an application from an activity in the JSON

	@returns: nothing
	'''
	def delete(self, name, activity):
		self.storage.deleteApplication(name, activity)