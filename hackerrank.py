def diagonalDifference(a):
    n = 3 
    x = sum([a[i][i] for i in range(n)])
    y = sum([a[i][-i - 1] for i in range(n)])
    print x ,y
    


def plusMinus(arr):
    zeroes = arr.count(0)/float(len(arr))
    positives = len([i for i in arr if i > 0])/float(len(arr))
    negatives = len([i for i in arr if i < 0])/float(len(arr))
    print round(positives,6) , round(negatives,6) , round(zeroes,6)


def solution(a): 
    a_map = {}
    for i in range(len(a)):
        a_map[a[i]] = i

    rep = 0 
    sorted_a = sorted(a)

    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            rep += 1 

            index_to_sort = a_map[ sorted_a[i] ]
            a_map[  a[i] ] = a_map[ sorted_a[i] ]
            a[i], a[index_to_sort] = sorted_a[i], a[i]
    return rep  

def miniMaxSum(arr):
    mini = sum(arr) - max(arr)
    maxi = sum(arr) - min(arr)
    print "%d %d" % (mini, maxi)

def timeConversion(s):
    new_time = 0 
    if s[-2:] == "PM" and s[0:2] != '12':
        new_time = str(int(s[0:2]) + 12)
    elif s[-2:] == 'PM' and s[0:2] == '12':
        new_time = s[0:2]
    if s[0:2] == '12' and s[-2:] == 'AM': 
        new_time = '00'
    if s[-2:] == "AM" and s[0:2] != '12' : 
        new_time = s[0:2]
    return new_time + s[2:-2]

def divisibleSumPairs(n, k, ar):
    counter = 0 
    for i in range(len(ar)):
        for j in range(len(ar)): 
            if (ar[i] + ar[j]) % k == 0 and i < j: 
                counter += 1
    return counter 
                

def migratoryBirds(n, ar):
    result = []
    x = max([ar.count(i) for i in ar]) 
    for i in ar: 
        if ar.count(i) == x: 
            result.append(i)
    return min(result)


def if_S(n):
    if n % 3 == 0 and n % 2 != 0: 
        print 'Weird' 
        return 1
    if n % 2 == 0 and n in range(2, 6):
        print "Not Weird"
        return 1
    if n % 2 == 0 and n in range(6,21):
        print "Weird"
        return 1
    if n % 2 == 0 and n > 20: 
        print "Not Weird"
        return 1 
        


def solve(grades):
    for i in grades:
        counter = 0 
        if i % 5 == 0: 
            print i
            continue 
        if i < 38: 
            print i 
            continue 
        for x in range(2): 
            i += 1 
            counter += 1
            if i % 5 == 0:
                print i 
                break
            elif i % 5 != 0 and counter == 2: 
                print i -2 
                break 
             
        

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # note the optimization here 
    x = [ i for i in apples if i + a <= t and i + a>= s ]
    y = [ i for i in oranges if (i + b) <= t and (i + b)>= s ]
    print len(x)
    print len(y)



    
def breakingRecords(score):
    lowest = score[0]
    highest = score[0]
    record_highs = 0
    record_lows = 0
    for i in score: 
        if i > highest: 
            highest = i 
            record_highs += 1
        elif i < lowest: 
            lowest = i 
            record_lows += 1 
    print record_highs, record_lows 

def countingValleys(s):
    dic = { "D": -1, "U": 1}
    counter = 0 
    sum = 0 
    curr = 0 
    for i in s: 
        sum += dic[i]
        curr = dic[i]
        if sum == 0 and curr == 1: counter += 1
    print counter 
    
#26/2/18
def getMoneySpent(keyboards, drives, s):
    curr = []
    for i in keyboards: 
        for k in drives:
            curr.append(i+k)
    curr = [i for i in curr if i <= s]
    return max(curr)

def solve(n, s, d, m):
    result = []
    counter = 0 
    for i in range(len(s)): 
        result.append(sum(s[i:i+m]))
        if i == (len(s) - 1):
            break 
    for i in result: 
        if i == d:  counter += 1
    return counter 

def sockMerchant(n, ar):
    set_socks = []
    for i in ar: 
        if i not in set_socks and ar.count(i) > 1: 
            #refreshes the set
            set_socks.append(i)
    return sum([(ar.count(i))/2 for i in set_socks]) # do this because the socks pairs of different color can be the same

from itertools import combinations

def pickingNumbers(a):
    results = [] 
    x = [ i for i in set(a)]
    for i in x: 
        counter = 0    
        for k in a: 
            if k == i+1: 
                counter += 1  
        results.append(sum([a.count(i), counter]))
    return max(results)
                

def kangaroo(x1, v1, x2, v2):
    #Bad optimization.Could be rectified another way by cases but lazy :)) or when x1 + steps*v1 == x2 + steps*v2
    kan_1 = x1
    kan_2 = x2
    
    for i in range(1000): 
        kan_1 += v1 
        kan_2 += v2
        if kan_1 == kan_2: return "YES"
    return "NO"

def catAndMouse(x, y, z):
    cat_a = abs(z -x)
    cat_b = abs(z - y)
    if cat_a < cat_b: 
        print "Cat A"
    elif cat_a > cat_b: 
        print "Cat B"
    else: 
        print "Mouse C"

catAndMouse(1,3,2)