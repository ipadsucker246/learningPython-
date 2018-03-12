def list_squared(m, n):
	devisors = []
	d = [i**2 for i in range(m,n*2) ] 
	for i in range(m, n+1):
		x = [x for x in range(1, i+1) if i%x == 0] 
		k = sum([z**2 for z in x])
		if k in d: 
			devisors.append([i,k]) 
	return devisors
		
print list_squared(1, 250) 


