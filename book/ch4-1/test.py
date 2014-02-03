#! /usr/bin/python
#Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.

long = "This is 3 a teit"
short = 4 

def isIn(x, y):
	x = str(x)
	y = str(y)
	if x in y or y in x:
		return True
	else:
		return False
print isIn(long, short)
