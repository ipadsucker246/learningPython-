def solution(digits): 
	cache = [] 
	while len(digits) >= 5: 
		max = int(digits[-5:])
		cache.append(max)   
		digits = digits[:-1]
	x = sorted(cache) 
	return x[-1]
	
print solution('1234567890')
