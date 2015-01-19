#! /usr/bin/env python3
l = []
n = 10
while n > 0:
    n -= 1 
    l.append(int(input('Enter an integer.'))) 
odds = [j for j in l if j % 2 != 0]

if len(odds) == 0:
    print('No odd numbers entered.')
else:
    print(max(odds))
