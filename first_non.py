def first_non_repeating_letter(string):
	if len(string) == 0: return ''
	for i in string.lower(): 
		if (string.lower()).count(i) == 1 : return string[list(string).index(i)]
	return ''
       
		
print first_non_repeating_letter("Stress") 