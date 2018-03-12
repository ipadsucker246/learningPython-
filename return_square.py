def square_digits(num):
    lst = list(str(num))
    lst_2 = [] 
    result = None
    for i in lst: 
        #print i 
        i = str(int(i) * int(i)) 
        lst_2.append(i) 
        #print lst_2
    for i in lst_2: 
        if result == None:
            result = i
        else: 
            result += i
    return int(result) 
	
# compare with 

def square_digits(num):
    ret = "" # note how this is an empty srting is created
    for x in str(num): #strings doesn't need go thru the list() method
        ret += str(int(x)**2) 
    return int(ret)