#Bisection algorithm
#Script para acertar un numero del 1 al 100
#utilizando el metodo de biseccion



print "Please think of a number between 0 and 100!"
low = 0
high = 100
middle = int((low+high)/2)
print "Is your secret number " + str(middle) + "?"
preg = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")


while preg != 'c':

    if preg == 'h':
        high = middle
        middle = int((low+high)/2)
        print "Is your secret number " + str(middle) + "?"
        preg = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

        
    elif preg == 'l':
        low = middle
        middle = int((low+high)/2)
        print "Is your secret number " + str(middle) + "?"
        preg = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")


    else:
        print "Sorry, I did not understand your input."
        print "Is your secret number " + str(middle) + "?"
        preg = raw_input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print "Game over. Your secret number was: " + str(middle)
