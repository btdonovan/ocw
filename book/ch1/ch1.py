#! /usr/bin/env python3

def sqrt(n):
    g = n / 2
    while abs(g*g - n) > 0.0000000000001:
        print(g)
        g = (g + n/g)/2
    return g

def real_sqrt(n):
    return n**0.5

def test(a, b):
    while b:
        a, b = b, a%b    
#        print(a, b)
    return a

for i in range(22):
    if i % 2 == 0:
        continue
    print(i)
