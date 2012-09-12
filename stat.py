# ECE 2524 Homework 2 Problem 3 Sumit Kumar
print "ACCOUNT SUMMARY"


amount_due = float ("0")
count_for_average = 0
count_second_loop = 0
max = float ("-inf")
min = float ("inf")
max_name = "initialize"
min_name = "initialize"

with open('account', 'r') as f:
    for line in f:
	count_for_average = count_for_average + 1
	count_second_loop = count_for_average
	str=line
	x=str.split()
	add = float(x[2])
	amount_due = amount_due+add
	
	if float(x[2]) > max:
		max = float(x[2])
	if float(x[2]) < min:
		min = float(x[2])
	
with open('account', 'r') as f:
    for line in f:
	str=line
	x=str.split()
	if float(x[2]) == max:
		max_name = x[1]
	if float(x[2]) == min:
		min_name = x[1]

print "Total amount owed:",amount_due
print "Average amount owed:", amount_due/count_for_average
print "Maximum amount owed =", max,"by",max_name
print "Minimum amount owed =", min,"by",min_name

