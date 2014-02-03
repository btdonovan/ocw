#! /usr/bin/python
##
##outBalance = float(raw_input('Enter the outstanding balance on your account: '))
##apr = float(raw_input('Enter your anual percentage rate as a decimal: '))
##minpay = float(raw_input('Enter your minimum montly payment rate as a decimal: '))
##mpr = apr/12.0
##totalPaid = 0.0
##for m in range(1, 13):
##    payment = round(minpay * outBalance, 2)
##    interest = round(mpr * outBalance, 2)
##    principal = payment - interest
##    outBalance -= principal
##    print 'Month:', m
##    print '   Minimum Payment:     $' + str(payment)
##    print '   Principal Paid:      $' + str(principal)
##    print '   Outstanding Balance: $' + str(outBalance)
##    totalPaid += payment
##
##print 'RESULT:'
##print 'Total amount paid: $' + str(totalPaid)
##print 'Remaining balance after 12 months: $' + str(outBalance)

### 6.00 PS1-A Solution
### Determines remaining credit card balance after a year of making the minimum payment each month
##
##balance = float(raw_input("Enter the outstanding balance on your credit card: "))
##annualInterestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
##minMonthlyPaymentRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
##
### Monthly Interest Rate
##monthlyInterestRate = annualInterestRate/12
##
### Initialize state variables
##numMonths = 1
##totalAmtPaid = 0
##
##while numMonths <= 12:
##    # Minimum monthly payment of balance at start of the month
##    minPayment = round(minMonthlyPaymentRate * balance,2)
##    totalAmtPaid += minPayment
##    
##    # Amt of monthly payment that goes to interest
##    interestPaid = round(monthlyInterestRate * balance,2)
##    
##    # Amt of principal paid off
##    principalPaid = minPayment - interestPaid
##    
##    # Subtract monthly payment from outstanding balance
##    balance -= principalPaid
##    
##    print "Month:", numMonths
##    print "Minimum monthly payment:", minPayment
##    print "Remaining balance:", balance
##    
##    # Count this as a new month     
##    numMonths += 1
##
##print "RESULT"
##print "Total amount paid:",totalAmtPaid
##print "Remaining balance:",balance

##outBalance = float(raw_input('Enter the outstanding balance on your account: '))
##apr = float(raw_input('Enter your anual percentage rate as a decimal: '))
##mpr = apr/12.0
##payment = 0
##newBalance = outBalance
####low = outBalance / 12
####high = (outBalance * (1 + mpr)) ** 12.0)/12.0
##while newBalance > 0:
##    for m in range(1, 13):
##        newBalance = newBalance * (1 + mpr) - payment
###        print newBalance
##        if newBalance < 0:
##            break
##    if newBalance > 0:
##        newBalance = outBalance
##        payment += 0.01
##print 'RESULT'
##print 'Monthly payment to pay of debt in 1 year:', payment
##print 'Number of months needed:', m
##print round(newBalance, 2)

##outBalance = float(raw_input('Enter the outstanding balance on your account: '))
##apr = float(raw_input('Enter your anual percentage rate as a decimal: '))
##mpr = apr/12.0
##newBalance = outBalance
##low = newBalance / 12
##high = (outBalance * (1 + mpr) ** 12)/12
###payment = 0
##while abs(newBalance) > 0.12 or newBalance > 0:
##    payment = round((low + high)/2.0, 2)
##    for m in range(1, 13):
##        newBalance = round(newBalance * (1 + mpr) - payment, 2)
##        if newBalance < 0:
##            break
##    if newBalance < 0:
##        high = payment
##    else:
##        low = payment
##    print newBalance
##    if abs(newBalance) > 0.12 or newBalance > 0:
##        newBalance = outBalance
##print 'RESULT'
##print 'Monthly payment to pay off debt in 1 year:', payment
##print 'Number of months needed:', m
##print 'Balance: ', newBalance

outBalance = float(raw_input('Enter the outstanding balance on your account: '))
apr = float(raw_input('Enter your anual percentage rate as a decimal: '))
mpr = apr/12.0
newBalance = outBalance
low = newBalance / 12
high = (outBalance * (1 + mpr) ** 12)/12
#payment = 0
while (high - low) > 0.005:
    payment = round((low + high)/2.0, 2)
    for m in range(1, 13):
        newBalance = round(newBalance * (1 + mpr) - payment, 2)
        if newBalance < 0:
            break
    if newBalance < 0:
        high = payment
    else:
        low = payment
    print newBalance
    if (high - low) > 0.005:
        newBalance = outBalance
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', payment
print 'Number of months needed:', m
print 'Balance: ', newBalance

### 6.00 PS1-C Solution
### Uses bisection search to find the fixed minimum monthly payment needed
### to finish paying off credit card debt within a year
##
### Retrieve input
##original_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
##interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
##
### Initialize state variables
##balance = original_balance
##low_payment = balance/12
##high_payment = (balance*(1+(interest_rate/12))**12)/12
##
### Use bisection search until the search space is sufficiently small
##while True:
##    balance = original_balance
##    monthly_payment = (low_payment + high_payment)/2
##
##    # Simulate passage of time until outstanding balance is paid off
##    # Each iteration represents 1 month
##    for month in range(1,13):
##        interest = round(balance*interest_rate/12, 2)
##        balance += interest - monthly_payment
##        if balance <= 0:
##            break
##        
##    if (high_payment - low_payment < 0.005):
##        # Bisection search space is small enough
##        # Print result
##        print "RESULT"
##
##        # Round monthly payment up to the nearest cent
##        monthly_payment = round(monthly_payment + 0.004999, 2)
##        print "Monthly payment to pay off debt in 1 year:", round(monthly_payment,2)
##
##        # Recompute remaining balance and the number of months needed
##        balance = original_balance
##        for month in range(1,13):
##            interest = round(balance*interest_rate/12, 2)
##            balance += interest - monthly_payment
##            if balance <= 0:
##                break
##        print "Number of months needed:", month
##        print "Balance:", round(balance,2)
##        break
##    elif balance < 0:
##        #Paying too much
##        high_payment = monthly_payment
##    else:
##        #Paying too little
##        low_payment = monthly_payment
##
##
