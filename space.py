import subprocess
from storage import *

'''
Class responsible for creating and controlling the creation of activities
'''

class Space:

	'''
	Create an instance of the Storage class
	'''
	def __init__(self):
		self.storage = Storage()


	'''
	Add an space to the JSON

	@returns: nothing
	'''
	def add(self, name):
		space_obj = {"space": name, "sources": []}
		self.storage.addSpace(space_obj)


	'''
	Delete the entire space from the JSON
	'''
	def delete(self, name):
		self.storage.deleteSpace(name)


	'''
	Start the space

	Applications are stored as a string array.
	Bash command 'open' each.

	@returns: nothing
	'''
	def start(self, name):
		space_obj = self.storage.getSpace(name)
		if space_obj == -1:
			print Colors.WARNING + 'This space does not exist.' + Colors.ENDC
			return

		for source in space_obj['sources']:
			subprocess.call(['open', source])


	