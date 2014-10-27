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

# s = 'zyxwvutsrqponmlkjihgfedcba'
bigstr = ''
bigstr2 = s[0]
i = 0
while i < len(s)-1:

    if s[i] <= s[i+1]:
        bigstr2 = bigstr2 + s[i+1]
    elif len(bigstr2) > len(bigstr):
        bigstr = bigstr2
        bigstr2 = s[i+1]
    else:
        bigstr2 = s[i+1]

#    print "i:", i, "   s[i]:", s[i], "   s[i+1]:", s[i+1], "   bigstr2:", bigstr2, "   bigstr:", bigstr
    i = i + 1

if len(bigstr2) > len(bigstr):
        bigstr = bigstr2

print "Longest substring in alphabetical order is: " + bigstr