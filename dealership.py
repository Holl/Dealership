dealershipDictionary = {}
customerDictionary = {}

class Dealership(object):
	def __init__(self, dealCode, address, manager):
		self.dealCode = dealCode
		self.address = address
		self.manager = manager
		self.trucks = {}
		self.minivans = {}

	def __repr__(self):
		return "Dealership: {0}".format(self.dealCode)

class Vehicle(object):
	def __init__(self, color, age, weight):
		self.color = color
		self.age = age
		self.weight = weight 

class Truck(Vehicle):
	def __init__(self, truckCode, towing):
		self.truckCode = truckCode
		self.towing = towing
		self.history = []

	def __repr__(self):
		return "Truck: {0}".format(self.truckCode)

class Minivan(Vehicle):
	def __init__(self, miniCode, seats, automaticDoors):
		self.miniCode = miniCode
		self.seats = seats
		self.automaticDoors = automaticDoors
		self.history = []


	def __repr__(self):
		return "Minivan: {0}".format(self.miniCode)

class Customer(object):
	def __init__(self, customerCode, name):
		self.customerCode = customerCode
		self.name = name
		self.trucks = {}
		self.minivans = {}

	def __repr__(self):
		return "Name: {0}.  Customer Code: {1}".format(self.name, self.customerCode)

def main():

	userInput = raw_input("What would you like to do?  You can add a (d)ealership, (v)ehicle, or (c)ustomer.  You can also (l)ist info, where you can transfer vehicles, or press (q) to quit. ")

	if userInput == "d":
		newDealCode = raw_input("Please enter a unique dealership code for this. ")
		newAddress = raw_input("Please enter the address for this dealership. ")
		newManager = raw_input("Please enter the manager's name. ")

		newDealership = Dealership(newDealCode, newAddress, newManager)

		dealershipDictionary[newDealCode] = newDealership

		print "The dealership has been stored."

		main()

	if userInput == "v":
		userInput = raw_input("What kind of vehicle?  It can be a (t)ruck or (m)inivan. ")
		if userInput == "t":
			newTruckCode = raw_input("Please enter a unique code for this truck. ")
			newColor = raw_input("Please enter a color: ")
			newAge = raw_input("How old is this car? ")
			newWeight = raw_input("How much does it weigh? ")
			newTowing = raw_input("How much can this motherf*cker tow? ")
			whichDealership = raw_input("Please enter the dealership code that this truck is in. ")

			newTruck = Truck(newTruckCode, newTowing)
			newTruck.age = newAge
			newTruck.weight = newWeight
			newTruck.color = newColor

			dealershipDictionary[whichDealership].trucks[newTruckCode] = newTruck

			print "Truck stored."

			print dealershipDictionary[whichDealership].trucks[newTruckCode]

			main()

		if userInput == "m":
			newMiniCode = raw_input("Please enter a unique code for this Minivan. ")
			newColor = raw_input("Please enter a color: ")
			newAge = raw_input("How old is this car? ")
			newWeight = raw_input("How much does it weigh? ")
			newSeats = raw_input("How many seats does it have? ")
			newAutomatic = raw_input("Are the doors automatic? y/n: ")
			whichDealership = raw_input("Please enter the dealership code that this truck is in. ")

			newMini = Minivan(newMiniCode, newSeats, newAutomatic)
			newMini.age = newAge
			newMini.weight = newWeight
			newMini.color = newColor

			dealershipDictionary[whichDealership].minivans[newMiniCode] = newMini

			print "Minivan stored."

			print dealershipDictionary[whichDealership].minivans[newMiniCode]

			main()

	if userInput == "c":
		newCustomerCode = raw_input("Please enter a unique code for this customer. ")
		newName = raw_input("What is this person's name? ")

		newCustomer = Customer(newCustomerCode, newName)

		customerDictionary[newCustomerCode] = newCustomer

		main()


	if userInput == "l":

		userInput = raw_input("Do you want to see a list of (d)ealerships or (c)ustomers? You can also go (b)ack. ")

		if userInput == "d":
			print "These are the stored dealerships:"
			print dealershipDictionary

			userInput = raw_input("Type the code of the dealership you want more information on. ")

			print dealershipDictionary[userInput]
			print "Location:"
			print dealershipDictionary[userInput].address
			print "Manged by:"
			print dealershipDictionary[userInput].manager
			print "Trucks:"
			print dealershipDictionary[userInput].trucks
			print "Minivans:"
			print dealershipDictionary[userInput].minivans

			userChoice = raw_input ("You can go (b)ack, or, you can get more info on (t)rucks or (m)inivans. ")

			if userChoice == "t":
				userChoice = raw_input ("Please enter the truck code for the truck you need more information on. ")

				print dealershipDictionary[userInput].trucks[userChoice]
				print "Color:"
				print dealershipDictionary[userInput].trucks[userChoice].color
				print "Age:"
				print dealershipDictionary[userInput].trucks[userChoice].age
				print "Weight:"
				print dealershipDictionary[userInput].trucks[userChoice].weight
				print "Towing:"
				print dealershipDictionary[userInput].trucks[userChoice].towing
				print "History:"
				print dealershipDictionary[userInput].trucks[userChoice].history

				transferer = raw_input("You can (t)ransfer this vehicle or go (b)ack to the main menu. ")
				if transferer == "b":
					main()
				if transferer == "t":
					transferer = raw_input("Transfer to a (c)ustomer or another (d)ealership?")
					if transferer == "c":
						print customerDictionary

						transferer = raw_input("Enter the customer code to sell the vehicle to. ")

						dealershipDictionary[userInput].trucks[userChoice].history.append(userInput)

						customerDictionary[transferer].trucks[userChoice] = dealershipDictionary[userInput].trucks[userChoice]

						del dealershipDictionary[userInput].trucks[userChoice]

						print "Transfer complete."

					if transferer == "d":
						print dealershipDictionary

						transferer = raw_input("Enter the dealership code to sell the vehicle to.")

						dealershipDictionary[userInput].trucks[userChoice].history.append(userInput)

						dealershipDictionary[transferer].trucks[userChoice] = dealershipDictionary[userInput].trucks[userChoice]

						del dealershipDictionary[userInput].trucks[userChoice]

						print "Transfer complete."



			if userChoice == "m":
				userChoice = raw_input("Please enter the minivan code for the minivan you need more information on. ")

				print dealershipDictionary[userInput].minivans[userChoice]
				print "Color:"
				print dealershipDictionary[userInput].minivans[userChoice].color
				print "Age:"
				print dealershipDictionary[userInput].minivans[userChoice].age
				print "Weight:"
				print dealershipDictionary[userInput].minivans[userChoice].weight
				print "Seats:"
				print dealershipDictionary[userInput].minivans[userChoice].seats
				print "Automatic Doors:"
				print dealershipDictionary[userInput].minivans[userChoice].automaticDoors
				print "History:"
				print dealershipDictionary[userInput].minivans[userChoice].history

				transferer = raw_input("You can (t)ransfer this vehicle or go (b)ack to the main menu. ")
				if transferer == "b":
					main()
				if transferer == "t":
					transferer = raw_input("Transfer to a (c)ustomer or another (d)ealership?")
					if transferer == "c":
						print customerDictionary

						transferer = raw_input("Enter the customer code to sell the vehicle to. ")

						dealershipDictionary[userInput].minivans[userChoice].history.append(userInput)

						customerDictionary[transferer].minivans[userChoice] = dealershipDictionary[userInput].minivans[userChoice]

						del dealershipDictionary[userInput].minivans[userChoice]

						print "Transfer complete."

					if transferer == "d":
						print dealershipDictionary

						transferer = raw_input("Enter the dealership code to sell the vehicle to.")

						dealershipDictionary[userInput].minivans[userChoice].history.append(userInput)

						dealershipDictionary[transferer].minivans[userChoice] = dealershipDictionary[userInput].minivans[userChoice]

						del dealershipDictionary[userInput].minivans[userChoice]

						print "Transfer complete."



			main()

			if userChoice == "b":
				main()

		if userInput == "c":
			print "These are the stored customers:"
			print customerDictionary

			userInput = raw_input("Type the code of the customer you want more information on. ")

			print customerDictionary[userInput]
			print customerDictionary[userInput].name
			print customerDictionary[userInput].trucks
			print customerDictionary[userInput].minivans

			userChoice = raw_input ("Would you like more info on (t)rucks or (m)inivans? ")

			if userChoice == "t":
				userChoice = raw_input ("Please enter the truck code for the truck you need more information on. ")

				print customerDictionary[userInput].trucks[userChoice]
				print "Color:"
				print customerDictionary[userInput].trucks[userChoice].color
				print "Age:"
				print customerDictionary[userInput].trucks[userChoice].age
				print "Weight:"
				print customerDictionary[userInput].trucks[userChoice].weight
				print "Towing:"
				print customerDictionary[userInput].trucks[userChoice].towing
				print "History:"
				print customerDictionary[userInput].trucks[userChoice].history

				transferer = raw_input("You can (t)ransfer this vehicle or go (b)ack to the main menu. ")
				if transferer == "b":
					main()
				if transferer == "t":
					transferer = raw_input("Transfer to a (c)ustomer or (d)ealership?")
					if transferer == "c":
						print customerDictionary

						transferer = raw_input("Enter the customer code to sell the vehicle to. ")

						customerDictionary[transferer].trucks[userChoice] = customerDictionary[userInput].trucks[userChoice]

						del customerDictionary[userInput].trucks[userChoice]

						print "Transfer complete."

					if transferer == "d":
						print dealershipDictionary

						transferer = raw_input("Enter the dealership code to sell the vehicle to.")

						dealershipDictionary[transferer].trucks[userChoice] = customerDictionary[userInput].trucks[userChoice]

						del customerDictionary[userInput].trucks[userChoice]

						print "Transfer complete."

			if userChoice == "m":
				userChoice = raw_input("Please enter the minivan code for the minivan you need more information on. ")

				print customerDictionary[userInput].minivans[userChoice]
				print "Color:"
				print customerDictionary[userInput].minivans[userChoice].color
				print "Age:"
				print customerDictionary[userInput].minivans[userChoice].age
				print "Weight:"
				print customerDictionary[userInput].minivans[userChoice].weight
				print "Seats:"
				print customerDictionary[userInput].minivans[userChoice].seats
				print "Automatic Doors:"
				print customerDictionary[userInput].minivans[userChoice].automaticDoors
				print "History:"
				print customerDictionary[userInput].minivans[userChoice].history

				transferer = raw_input("You can (t)ransfer this vehicle or go (b)ack to the main menu. ")
				if transferer == "b":
					main()
				if transferer == "t":
					transferer = raw_input("Transfer to a (c)ustomer or another (d)ealership?")
					if transferer == "c":
						print customerDictionary

						transferer = raw_input("Enter the customer code to sell the vehicle to. ")

						customerDictionary[transferer].minivans[userChoice] = customerDictionary[userInput].minivans[userChoice]

						del customerDictionary[userInput].minivans[userChoice]

						print "Transfer complete."

					if transferer == "d":
						print dealershipDictionary

						transferer = raw_input("Enter the dealership code to sell the vehicle to.")

						dealershipDictionary[transferer].minivans[userChoice] = customerDictionary[userInput].minivans[userChoice]

						del customerDictionary[userInput].minivans[userChoice]

						print "Transfer complete."

			main()

		if userInput == "b":
			main()

	if userInput == "q":
		exit()


main()


