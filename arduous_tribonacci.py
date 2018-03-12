def tribonacci(signature, n):
    while signature[-1] < n:
        if sum(signature[-3:]) > n:
             break 
        signature.append(sum(signature[-3:]))
    return signature 
      
print tribonacci([1,1,1], 6) 