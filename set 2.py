import pandas

class consumable:
	movies = list()
	books = list()
	series = list()
	consumption_time = 0


	text = ''' Enter: 1 for Books
		2 for Movies
		3 for Series

		'''


	def add_consumable(self):

		choice = input(self.text)

		def take_input():
			name = input("\nEnter Book name: ")
			rating = input("\nEnter rating: ")
			days_consumed = input("\n Enter days consumed: ")
			start_date = input("\n Enter Start date: ")
			end_date = input("\n Enter End date: ")


			keys = ["Name", "rating", "days_consumed", "start_date", "end_date"]

			return(dict(zip(keys, [name, rating, days_consumed, start_date, end_date])))


		if choice == '1':
			#print(take_input())
			consumable.books.append(take_input())
		if choice == '2':
			consumable.movies.append(take_input())
		if choice == '3':
			consumable.series.append(take_input())


	def see_list(self):
		choice = input(self.text)

		if choice == '1':
			#print(take_input())
			print(consumable.books)
		if choice == '2':
			print(consumable.movies)
		if choice == '3':
			print(consumable.series)



s = ''' Enter: 1. Add a consumable
		2. Edit a consumable
		3. Delete a consumable
		4. See the list of consumables and individually
		5. See overall info
		'''

#option = input(s)

obj = consumable()
obj.add_consumable()
obj.see_list()