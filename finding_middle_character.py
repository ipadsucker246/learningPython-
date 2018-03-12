def get_middle(s):
    index = None 
    index_2 = None
    boolean = None
    result = None
    lst = list(s)
    if len(lst)%2 == 0:
        boolean = True 
    else: 
        boolean = False 
    if boolean == True: 
        index = len(lst) / 2 
        index_2 = index - 1
        result = lst[index_2] + lst[index] 
		# result = lst[index_2: index] wont work since it returns a list 
    else: 
        index = (len(lst) - 1)/2
        result = lst[index] 
    return result 
	
# arr[x:y] returns a list object 
# refactor this code to 1 line if you can 