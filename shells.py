# ECE 2524 Homework 2 Problem 1 Sumit Kumar

with open('/etc/passwd', 'r') as f:
    for line in f:
	str=line
	x=str.split(":")
	print x[0],"\t",x[6]
