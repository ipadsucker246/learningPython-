str = 'nanananannananananananananna BAtman!' 
def maskify(cc):
    return  ''.join(['#' for x in cc[0:-4]]) + cc[-4:] 
	
print maskify(str) 