#-------------------------------------------------------------------------------
# Name:        PS2.1 PAYING THE MINIMUM
#-------------------------------------------------------------------------------
# Name:        PS2.2 PAYING DEBT OFF IN A YEAR
# Purpose:
#
# Author:      lmdefrancisco
#
# Created:     05/09/2014
# Copyright:   (c) lmdefrancisco 2014
# Licence:     GPL
#-------------------------------------------------------------------------------
#balance = 3926
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

bal = balance
air = annualInterestRate
minMonPay = 10
upb = balance

while bal > 0:
    bal = balance
    for i in range(0, 12):
        upb = bal - minMonPay
        bal = upb + ((air/12)*upb)
    minMonPay = minMonPay + 10

minMonPay = minMonPay - 10
print "Lowest Payment: ", minMonPay