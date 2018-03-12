def find_missing(arr):
	step= (arr[-1]- arr[0])/len(arr) 
	x,y = arr[0], (arr[-1]+1)
	k = list(set(range(x,y,step)) - set(arr))[0]
	return k 	
print find_missing([1, 3, 4, 5, 6, 7, 8, 9])


