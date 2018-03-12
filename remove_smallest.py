def remove_smallest(numbers): 
	numbers.remove(min(numbers)) 
	return numbers 
print remove_smallest([2,2,1,2,1]) 