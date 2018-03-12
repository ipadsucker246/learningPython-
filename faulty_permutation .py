def choose_best_sum(t, k, ls):
    results = []
    split = 0
    z = [] 
    for i in ls: 
        z = [x for x in ls if x != i]
        for x in z: 
            if len(z[z.index(x):]) >= k -1: 
                results.append(sum(z[z.index(x):z.index(x)+k-1],i))		
            if len(z[z.index(x):]) == k-1: 
                results.append(sum(z[-k:],i))
    filt = [d for d in results if d <= t]
    if len(filt) == 0: 
        return None 
    else: 
        return max(filt) 
	
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

print choose_best_sum(4832,10,ls) 

or you could do it much easier wwith itter.tools
