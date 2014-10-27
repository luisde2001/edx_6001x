#-------------------------------------------------------------------------------
# Name:        Problem Set 1.1 Counting Vowels
# Purpose: Counts the vowels from a string given.
#
# Author:      lmdefrancisco
#
# Created:     04/09/2014
# Copyright:   (c) lmdefrancisco 2014
# Licence:     GPL
#-------------------------------------------------------------------------------

# s = 'uuuxaqrwadjwgoixsdocao'
numVowels = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in vowels:
        numVowels = numVowels + 1
print "Number of vowels: " + str(numVowels)
