def maxSequence(arr): 
	curr, max = 0, 0 
	for i in arr: 
		print curr, max 
		curr += i 
		if curr < 0: curr = 0 
		if curr > max: max = curr 
	return max

print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

k = [1,2,3] 

