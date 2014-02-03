#! /usr/bin/python

# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root^pwr is equal to the integer entered by the user.  If no such pair of integers exists, it should print a message to that effect.

number = int(raw_input('Enter a whole number: '))
root = abs(number)
guess = 0
while abs(root) <= abs(number):
	pwr = 1
	while pwr < 6:
		if root**pwr == number:
			print root, 'raised to the power of', pwr, 'equals', str(number) + '.'
		pwr += 1
	root -= 1
# Note that this specification will include the number 1 as a power.  A number raised to the power of one will equal itself.  This program will always produce a valid output so the code required to print a message saying that no such integers exist will never run.  Bad specification.
