import pandas
class consumable:
	movies = list()
	books = list()
	series = list()

	movie_consumption_time = 0
	books_consumption_time = 0
	series_consumption_time = 0

	movie_days = 0
	book_days = 0
	series_days = 0
	#total_consumption_time


	text = ''' Enter: 1 for Books
		2 for Movies
		3 for Series

		'''




#--------------------------------------------------------------------------------add
	def add_consumable(self):

		choice = input(self.text)

		def take_input():#returns dictionary of inputs
			name = input("Enter name: ")
			rating = float(input("Enter rating: "))
			consumption_time = int(input("Enter total consumption time(hr's): "))
			days_consumed = int(input("Enter days consumed: "))
			start_date = input("Enter Start date: ")
			end_date = input("Enter End date: ")

			#create dictionary-------------------------
			keys = ["Name", "Rating", "Days consumed", "Start date", "End date", "Consumption time"]
			return(dict(zip(keys, [name, rating, days_consumed, start_date, end_date, consumption_time])))


		if choice == '1':
			#print(take_input())
			dictionary = take_input()
			#calculate consumption time-------------
			consumable.books_consumption_time += dictionary.get("Consumption time") * dictionary.get("Days consumed")
			consumable.book_days += dictionary.get("Days consumed")

			consumable.books.append(dictionary)


		if choice == '2':
			dictionary= take_input()
			#calculate consumption time
			consumable.movie_consumption_time +=  dictionary.get("Consumption time") * dictionary.get("Days consumed")
			consumable.movie_days += dictionary.get("Days consumed")

			consumable.movies.append(dictionary)


		if choice == '3':
			dictionary = take_input()
			#calculate consumption time
			consumable.series_consumption_time +=  dictionary.get("Consumption time") * dictionary.get("Days consumed")
			consumable.series_days += dictionary.get("Days consumed")

			consumable.series.append(dictionary)












#--------------------------------------------------------------------------------edit
	def edit_consumable(self):
		choice = input(self.text)
		name = input("\nEnter Product name to be edited: ")



		def input_edits():
			inc_consumed_time = int(input("Enter added hr's of consumption: "))
			inc_days_consumed = input("Add a day to days of consumption(1=Yes/0=No): ")
			new_rating = float(input("New rating: "))
			end_date = input("Enter consumption ending date: ")
			return(inc_consumed_time, inc_days_consumed, new_rating, end_date)

		#def commit_edits():


		if choice =='1':
			inc_consumed_time, inc_days_consumed, new_rating, end_date = input_edits()

			for index,item in enumerate(consumable.books):

				if item.get("Name") == name:#select the dictionary to be edited

					if inc_days_consumed == "1":
						consumable.books[index]["Days consumed"] += 1
						consumable.books[index]["Consumption time"] += inc_consumed_time
						consumable.books_consumption_time += consumable.books[index]["Consumption time"]
						consumable.book_days += 1

					if new_rating is not None:
					    consumable.books[index]["Rating"] = new_rating

					if end_date is not None:
					    consumable.books[index]["end date"] = end_date

					break


		if choice =='2':
			inc_consumed_time, inc_days_consumed, new_rating, end_date = input_edits()

			for index,item in enumerate(consumable.movies):

				if item.get("Name") == name:#select the dictionary to be edited

					if inc_days_consumed == "1":
						consumable.movies[index]["Days consumed"] += 1
						consumable.movies[index]["Consumption time"] += inc_consumed_time
						consumable.movie_consumption_time += consumable.movies[index]["Consumption time"]
						consumable.movie_days += 1

					if new_rating is not None:
					    consumable.movies[index]["Rating"] = new_rating

					if end_date is not None:
					    consumable.movies[index]["end date"] = end_date

					break


		if choice =='3':
			inc_consumed_time, inc_days_consumed, new_rating, end_date = input_edits()

			for index,item in enumerate(consumable.series):

				if item.get("Name") == name:

					if inc_days_consumed == "1":
						consumable.series[index]["Days consumed"] += 1
						consumable.series[index]["Consumption time"] += inc_consumed_time
						consumable.series_consumption_time += consumable.series[index]["Consumption time"]
						consumable.series_days += 1

					if new_rating is not None:
					    consumable.series[index]["Rating"] = new_rating

					if end_date is not None:
					    consumable.series[index]["end date"] = end_date
					break






#--------------------------------------------------------------------------------see list
	def see_list(self):
		choice = input(self.text)

		if choice == '1':
			for item in self.books:
				dataframe = pandas.DataFrame(list(item.items()))
				print(dataframe.to_string(index = False))
		if choice == '2':
			for item in self.movies:
				dataframe = pandas.DataFrame(list(item.items()))
				print(dataframe.to_string(index = False))
		if choice == '3':
			for item in self.series:
				dataframe = pandas.DataFrame(list(item.items()))
				print(dataframe.to_string(index = False))









#--------------------------------------------------------------------------------delete
	def delete_consumbale(self):
		choice = input(self.text)
		name = input("\nEnter Product name to be deleted: ")
		if choice =='1':
			for index,item in enumerate(consumable.books):
				if item.get("Name") == name:
					del consumable.books[index]
		if choice =='2':
			for index,item in enumerate(consumable.movies):
				if item.get("Name") == name:
					del consumable.movies[index]
		if choice =='3':
			for index,item in enumerate(consumable.series):
				if item.get("Name") == name:
					del consumable.series[index]










	def see_all_info(self):

		#avg rating calculation--------
		avg_movie_rating =0
		avg_book_rating =0
		avg_series_rating =0

		i=0
		for item in consumable.books:
			if item.get("Rating") is not None:
				i+=1
				avg_book_rating += item.get("Rating")
		if i!=0:
			avg_book_rating = avg_book_rating / i


		j=0
		for item in consumable.movies:
			if item.get("Rating") is not None:
				j+=1
				avg_movie_rating += item.get("Rating")
		if j!= 0:
			avg_movie_rating = avg_movie_rating / j


		k=0
		for item in consumable.series:
			if item.get("Rating") is not None:
				k+=1
				avg_series_rating += item.get("Rating")
		if k!=0:
			avg_series_rating = avg_series_rating / k



		details = {
				"Total number of consumables": len(self.books)+len(self.series)+len(self.movies),
				"Total Books read": len(self.books),
				"Total Movies watched": len(self.movies),
				"Total Series finished": len(self.series),
				"Total consumption time" : self.movie_consumption_time + self.books_consumption_time + self.series_consumption_time,
				"Movie Consumption time" : self.movie_consumption_time,
				"Series Consumption time" : self.series_consumption_time,
				"Books Consumption time": self.books_consumption_time,
				"Total days of consumption" : self.movie_days + self.book_days + self.series_days,
				"Avg rating of all consumables": (avg_movie_rating + avg_series_rating + avg_book_rating)/(i+j+k),
				"Avg Movie rating" : avg_movie_rating,
				"Avg Series rating" : avg_series_rating,
				"Avg Book rating" : avg_book_rating
				}
		#print(details)
		dataframe = pandas.DataFrame(list(details.items()))
		print(dataframe.to_string(index = False))




s = ''' Enter: 1 to Add a consumable
		2 to Edit a consumable
		3 to Delete a consumable
		4 to See the list of consumables individually
		5 to See overall info
		6 to exit
		'''
obj = consumable()

while 1:
	option = int(input(s))
	if option == 1:
		obj.add_consumable()

	if option ==2:
		obj.edit_consumable()

	if option == 3:
		obj.delete_consumbale()

	if option == 4:
		obj.see_list()

	if option == 5:
		obj.see_all_info()

	if option == 6:
		break

