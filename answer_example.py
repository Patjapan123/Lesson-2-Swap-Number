def swap(list): #a function that swap the number in a list of two
	if len(list != 2): #total number of list not 2 code no work
		raise ValueError("Invalid Swap List") #error (invalid swap list)
	third_cup = list[0] # third cup is the first term
	list[0] = list[1] # first term swap second term
	list[1] = third_cup # second term is third cup(first term)
	return list #return list