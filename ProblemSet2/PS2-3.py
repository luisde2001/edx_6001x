#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:        PS2.3 PAYING DEBT OFF IN A YEAR BISECTION
# Purpose:
#
# Author:      lmdefrancisco
#
# Created:     05/09/2014
# Copyright:   (c) lmdefrancisco 2014
# Licence:     GPL
#-------------------------------------------------------------------------------
#balance = 999999
#annualInterestRate = 0.18

bal = balance
air = annualInterestRate
upb = balance
monthlow = bal / 12
monthhigh = (bal*((1+air)**12))/12
minMonPay = 0

while bal > 0.01:
    bal = balance
    minMonPay = (monthlow+monthhigh)/2
    for i in range(0, 12):
        upb = bal - minMonPay
        bal = upb + ((air/12)*upb)
    if bal > 0.01:
        monthlow = minMonPay
    elif bal < -0.01:
        monthhigh = minMonPay
        bal = abs(bal)
    else:
        print "Lowest Payment: %.2f" %minMonPay
