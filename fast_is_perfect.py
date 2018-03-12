def isPP(n):  
	results = None
	for i in range(2, int(n**0.5 + 1)): 
		m = n 
		counter = 0 
		while m % i == 0: 
			m = m/i 
			counter += 1  
		if m == 1  and i ** counter == n: 
			results = [i, counter]
			break 
	return results
	
