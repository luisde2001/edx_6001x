#-------------------------------------------------------------------------------
# Name:        PS2.1 PAYING THE MINIMUM
# Purpose:
#
# Author:      lmdefrancisco
#
# Created:     05/09/2014
# Copyright:   (c) lmdefrancisco 2014
# Licence:     GPL
#-------------------------------------------------------------------------------
#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

bal = balance
air = annualInterestRate
mpr = monthlyPaymentRate
payed = 0

for i in range(0, 12):
    print "Month: " , i+1
    minMonPay = bal * mpr
    upb = bal - minMonPay
    bal = upb + ((air/12)*upb)
    payed = payed + minMonPay
    print "Minimum monthly payment: %.2f" %minMonPay
    print "Remaining balance: %.2f" %bal

print "Total paid: %.2f" %payed
print "Remaining balance: %.2f" %bal
