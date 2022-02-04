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
			name = input("\nEnter name: ")
			rating = input("\nEnter rating: ")
			days_consumed = input("\nEnter days consumed: ")
			start_date = input("\nEnter Start date: ")
			end_date = input("\nEnter End date: ")

			keys = ["Name", "Rating", "Days consumed", "Start date", "end date"]
			return(dict(zip(keys, [name, rating, days_consumed, start_date, end_date])))


		if choice == '1':
			#print(take_input())
			consumable.books.append(take_input())
		if choice == '2':
			consumable.movies.append(take_input())
		if choice == '3':
			consumable.series.append(take_input())


	def edit_consumable(self):
		choice = input(self.text)
		name = input("\nEnter Product name to be edited: ")

		def input_edits():
			inc_consumed_time = input("\nEnter added hr's of consumption: ")
			inc_days_consumed = input("\nAdd a day to days of consumption(1=Yes/0=No): ")
			new_rating = input("\nNew rating: ")
			end_date = input("\nEnter consumption ending date: ")
			return(inc_consumed_time, inc_days_consumed, new_rating, end_date)





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