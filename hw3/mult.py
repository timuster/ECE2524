# ECE 2524 Homework 3 Problem 1 Sumit Kumar

import sys
import argparse

parser = argparse.ArgumentParser(description='Process some numbers')
args = parser.parse_args()


print "Enter numbers to multiply"
f=0
ans=1

try:	
	while f==0:
		var1 = raw_input("Enter Number: ")
		x= float(var1)
		ans=ans*x

except EOFError:
	print "\nEnd of file command has been received!"
	print "\nHere is your answer :", ans

except ValueError as e:
	print "Could not convert string to float: ", var1 #check sys.st
	sys.exit(1)


