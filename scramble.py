def scramble(s1,s2):
	x = []
	for i in set([i for i in s2 if i in s1]): 
		if s1.count(i) >= s2.count(i): 
			x.append(True)
		else: 
			x.append(False) 
	if False in x: return False
	else: return True 
print scramble('cedewaraaossoqqyt','codewars')