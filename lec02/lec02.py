#! /usr/bin/python

##x = 3  #Create variable x and assign value 3 to it
##x = x*x  #Bind x to value 9
##print x
##y = raw_input('enter a number:')
##print type(y)
##print y
##y = float(raw_input('Enter a number: '))
##print type(y)
##print y
##print y*y
##
##x = int(raw_input('Enter an integer: '))
##if x%2 == 0:
##    print 'Even'
##else:
##    print 'Odd'
##    if x%3 != 0:
##        print 'And not divisible by 3'
##
##x = int(raw_input('Enter x: '))
##y = int(raw_input('Enter y: '))
##z = int(raw_input('Enter z: '))
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##else:
##    print 'y is least'
##
##if x < y:
##    if x < z:
##        print 'x is least'
##    else:
##        print 'z is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'  
##
##if x < y and x < z:
##    print 'x is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'
##    
##
#Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    #print 'current guess =', ans
    #While loop continues to increment the value of ans until ans*ans*ans is equal or greater than abs(x)
    #Once the value of ans*ans*ans is equal or greater than abs(x) the while loop ends.
if ans*ans*ans != abs(x):
    print x, 'is not a perfect cube'
    #The while loop incremented ans until ans**3 was equal or greater than abs(x).
    #Now we test to see which condition was the case.  If ans**3 is greater than abs(x) we end the program now.
    #x is not a perfect cube.
else: 
    #Now we get to cases where x is a perfect cube
    if x < 0: 
        #Negative numbers can be perfect cubes. Test if x is negative.
        #if x is negative, make ans negative. Otherwise do nothing.
        ans = -ans 
    #At this point, we know x is a perfect cube and we know the value of the cube root.
    #Print our results.
    print 'Cube root of ' + str(x) + ' is ' + str(ans)

##
##
##
##
