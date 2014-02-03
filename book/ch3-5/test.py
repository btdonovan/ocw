#! /usr/bin/python

#Newton-Raphson for square root
#find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.0001
y = float(raw_input('Enter a number: '))
guess = y/2.0
nrguess = 0
while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2) - y)/(2*guess))
	nrguess += 1
print 'Square root of', y, 'is about', guess

bsguess = 0

low = -abs(y)
high = abs(y)
ans = (high + low)/2.0
while abs(ans**2 - y) >= epsilon:
	bsguess += 1
	if ans**2 < y:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print 'Square root of', y, 'is about', ans

if nrguess < bsguess:
	print 'Newton-Raphson beat bisection by', bsguess - nrguess 
else:
	print 'Bisection beat Newton-Raphson by', nrguess - bsguess 
