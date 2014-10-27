#-------------------------------------------------------------------------------
# Name:         Problem Set 1.3 Alphabetical Substrings
# Purpose:      Finds the longest alphbetical substring  in a given string.
#
# Author:       lmdefrancisco
#
# Created:      04/09/2014
# Copyright:    (c) lmdefrancisco 2014
# Licence:      GPL
#-------------------------------------------------------------------------------

# s = 'bobobobasdajeusdjfbobob'
numbobs = 0
i = 0
while i <= len(s):
    si = s[i:(i+3)]
    numbobs = numbobs +  si.count('bob')
    i = i+1
print "Number of times bob occurs is: " + str(numbobs)