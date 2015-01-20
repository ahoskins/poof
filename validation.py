import os

class Validation:

	'''
	Check is given application name exists in /Applications/

	@returns: boolean
	'''
	def checkMatch(self, name):
		if name + '.app' in os.listdir('/Applications/'):
			return True

		return False 
