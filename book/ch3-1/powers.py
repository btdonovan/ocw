#! /usr/bin/env python3

def finger(number):
    """
    Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root^pwr is equal to the integer entered by the user.  If no such pair of integers exists, it should print a message to that effect.
    
    Note that this specification will include the number 1 as a power.  A number raised to the power of one will equal itself.  This program will always produce a valid output so the code required to print a message saying that no such integers exist will never run.  Bad specification.
    """
    root = abs(number)
    while abs(root) <= abs(number):
            pwr = 1
            while pwr < 6:
                    if root**pwr == number:
                            print(root, 'raised to the power of', pwr, 'equals', str(number) + '.')
                    pwr += 1
            root -= 1

def pCube(x):
    """Find the cube root of a perfect cube."""
    ans = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print('Cube root of ' + str(x) + ' is ' + str(ans))

def testMax(max):
    i = 0
    while i < max:
        i = i + 1
    print(i)
