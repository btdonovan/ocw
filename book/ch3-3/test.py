#! /usr/bin/python

x = 25000302302653.0
epsilon = 0.01
numGuesses = 0
low = -abs(x) 
high = abs(x) 
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
	print 'low =', low, 'high =', high, 'ans =', ans
	numGuesses += 1
	if ans**3 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x
