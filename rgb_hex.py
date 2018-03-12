def rgb(r, g, b):
	dic = { 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',14 : 'E', 15 : 'F'}
	results = [] 
	color = [r,g,b]
	for i in color:
		num1 = i/16 
		num2 = i % 16
		if num1 >= 16: 
			num1 = 'F'
			num2 = 'F'
		if num1 > 9 and num1 < 16 : num1 = dic[num1] 
		if num2 > 9 and num2 < 16: num2 = dic[num2] 
		if num1 < 0: 
			results.append('00') 
		else:
			results.append(''.join([str(num1),str(num2)])) 
	return ''.join(results) 

print rgb(79,245,1000)