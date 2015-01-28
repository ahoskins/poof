import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from colors import *

class Validation:

	'''
	Check is given application name exists in /Applications/

	Returns True if the given name has an exact math in /Applications/

	@returns: boolean
	'''
	def matchAgainstDirectory(self, name):
		if name in os.listdir('/Applications/'):
			return True

		return False


	'''
	Do fuzzy comparison of application name with a string in /Applications/

	Return either the successful result or None

	@returns: String or None
	'''
	def fuzzyAgainstDirectory(self, name):
		choices = os.listdir('/Applications/')
		fuzzy_result = process.extractOne(name, choices)

		if fuzzy_result[1] > 80:
			print Colors.OKBLUE + 'Did you mean "' + fuzzy_result[0] + '"? Yes or no:' + Colors.ENDC
			pick = raw_input('--> ')
			if pick == 'Yes' or pick == 'yes' or pick == 'y':
				return fuzzy_result[0]

		else:
			print Colors.WARNING + 'No match in /Applications/' + Colors.ENDC
			return None
