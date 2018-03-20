def tidy_number(n): 
    # return the last number that each and every element in the number has to be placed from low to high etc: 132 must return 129 
    #pre-requisites: make a new string of the integer so that we can loop through it 
                   # make a cache list_type varibale so we can store individual numbers in the str above as we loop thru it 
                     
    
    str_number = str(n) 
    cache = [] 
    untidied_part = []  
    result = ''
     
     # loop through the str_integer 
     
    for i in range(len(str_number)):
        # at firrst the cache will be empty so we have to append the first element of the str_int 
        if len(cache) == 0: 
            cache.append(int(str_number[i])) 
            continue 
            
     # if the current number is < the last numebr we looped through, break. Now comes the fun part. 
     # for example: as we loop through say "123325" we'll have designated where our numebr is not "tidy" ("32"). 
     # we would assign "3325" as the untidied part. THe reason for that is that, if we only tidy "325", our number would be like this "123299" 
     # since "325" can only be subtracted to find the closest tidied number we can subtract it to "299", but then if there was any  
     # multiple of the biggest number in the untidied_part('3') previously in the cache, we would create an untidied number. 
        
     # The basics steps of our algo wil be: loop through the number, find the number smaller than the precedent number, find the 
     # first index in the str_int of the precedent number, return tidied_part +  untidied_part as the precedent number* powers of 10 -1 
       
      
        if int(str_number[i]) < cache[-1]: 
            untidied_part = str_number[cache.index(cache[-1]):]
            break 
        cache.append(int(str_number[i]))
    if len(untidied_part) == len(str_number): 
        result = untidied_part[0] + '0'*(len(untidied_part) - 1 ) 
        return int(result) - 1 
    elif len(untidied_part) != len(str_number): 
        str_number = str_number[0:len(str_number)-len(untidied_part)]
        untidied_part = untidied_part[0] + '0'*(len(untidied_part) - 1 )

        result = str_number + untidied_part 
        return int(result) - 1 

 
