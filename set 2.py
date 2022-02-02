class consumable:

	def __init__(self, type):
		self.type = type


s = ''' Enter: 1. Add a consumable
		2. Edit a consumable
		3. Delete a consumable
		4. See the list of consumables and individually
		5. See overall info
		'''

option = input(s)