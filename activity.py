from storage import *

'''
Class responsible for creating and controlling the creation of activities
'''

class Activity:
	
	'''
	Create an instance of the Storage class
	'''
	def __init__(self):
		self.storage = Storage()


	'''
	Add an activity to the JSON

	@returns: nothing
	'''
	def add(self, name):
		activity_obj = {"activity": name, "sources": []}
		self.storage.addActivity(activity_obj)


	'''
	Delete the entire activity from the JSON
	'''
	def delete(self, name):
		self.storage.deleteActivity(name)


	'''
	Start the activity

	Applications are stored as a string array.
	Bash command 'open' each.

	@returns: nothing
	'''
	def start(self, name):
		activity_obj = self.storage.getActivity(name)
		if activity_obj == -1:
			print name + ' does not exist.'

		for source in activity_obj['sources']:
			os.system('open ' + source + '.app')


	