def narcissistic( value ):
    result = 0 
    for i in list(str(value)): 
        result += int(i) ** len(str(value))
    if value == result: return True 
    return False 
	
a = range(0,100) 

