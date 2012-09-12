# ECE 2524 Homework 2 Problem 2 Sumit Kumar
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open('account', 'r') as f:
    for line in f:
	str=line
	x=str.split()
	if 'Blacksburg' in x:
		str=", "
		seq=x[4],x[1],x[0],x[2]
		print str.join(seq)


