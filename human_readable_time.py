def make_readable(seconds):
	hour = str(seconds/3600) 
	min = str((seconds%3600)/60)
	sec = str((seconds%36000)%60)
	if len(hour) == 1: hour = "0%s" % hour 
	if len(min) == 1: min = "0%s" % min 
	if len(sec) == 1: sec = "0%s" % sec
	return "%s:%s:%s" % (hour,min,sec)
	
print make_readable(366)
