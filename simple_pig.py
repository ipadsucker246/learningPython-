def pig_it(text):
	result = [] 
	split = '' 
	for i in text.split(): 
		if i in '!.,;':
			result.append(i) 
		else:	
			split = i[1:] + i[0] + 'ay' 
			result.append(split) 
	return " ".join(result) 

print pig_it('Pig latin, is cool !') 
		
print "fuck, this".split()