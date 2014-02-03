#! /usr/bin/python

oBalance = float(raw_input('Enter your account balance: '))
apr = float(raw_input('Enter your APR as a decimal: '))

mpr = apr/12
balance = oBalance
high = (balance * (1 + mpr)**12)/12
low = balance / 12

while True:
    balance = oBalance
    payment = (high + low)/2
    for m in range(1,13):
        interest = round(balance*apr/12, 2)
        balance += interest - payment
        if balance <= 0:
            break
    print m
    print balance
    print payment
    if (high - low) < 0.005:
        print 'RESULTS'
        payment = round(payment + 0.004999, 2)
        balance = oBalance
        for m in range(1, 13):
#            balance += round((balance * mpr), 2) - payment
            interest = round(balance*apr/12, 2)
            balance += interest - payment
            if balance <= 0:
                break
        print 'Months:', m
        print 'Balance:', round(balance, 2)
        print 'Payment:', round(payment, 2)

        break
    elif balance > 0:
        low = payment
    else:
        high = payment
    
