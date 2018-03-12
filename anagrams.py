def anagrams(word, words):
	results = [x for x in words if sorted(word) == sorted(x) ] 
	return results 
	
print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])