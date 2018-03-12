count_dic = {0 : '', 1: '-thousand', 2: '-million', 3:'-billion', 4:'-thousand-billion', 5:'-MILLION-BILLION', 6:'-TRILLION!'}
small_dic = {0 : 'hundred', 1: 'ty', 2: ''}
dic_change = { '2':'twen','3': 'thir', '4':'for','5':'fif', '6':'six', '7':'seven', '8':'eigh', '9':'nine'}
dic = {'0' : '' ,'1':'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve'}
def teen(s):  
    if s == 0: return ''
    elif str(s) in dic: return dic[str(s)]
    k = str(s)
    if k[1] in dic_change and k[0] == '1' and k not in dic:
        return dic_change[k[1]] + 'teen'     
    elif k in dic: return dic[k]
    elif k[0] != '1' and k[1] != '0': 
        return dic_change[k[0]] + 'ty' + '-' + dic[k[1]]
    elif k[0] != '1' and k[1] == '0': 
        return dic_change[k[0]] + 'ty'
    
def hundred(s): 
    z = str(s)
    x = int(z[1:]) 
    result = '' 
    result += dic[z[0]] + '-' + 'hundred' + '-' + teen(x)
    if  x == 0: 
        result = dic[z[0]] + '-' + 'hundred'
        return result 
    return result 

def number(n): 
    s = str(n)
    part = 0
    result = []
    speech = ''
    while len(s) >= 3: 
        part = int(s[-3:])
        s = s[:-3]
        result = [part] + result
    if len(s) != 0: result = [int(s)] + result
    result = result[::-1]  
    for i in range(len(result)): 
        cu = result[i]
        if len(str(cu)) == 3 and cu != 0:
            speech = hundred(cu) + count_dic[i] + ' ' + speech
        elif len(str(cu)) == 2 and cu != 0: 
            speech = teen(cu)  +  count_dic[i] + ' ' + speech 
        elif len(str(cu)) == 1 and cu != 0: 
            speech = dic[str(cu)] + count_dic[i] + ' ' + speech 
    return speech
print number()