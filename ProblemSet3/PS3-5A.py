def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    wordLength = len(secretWord)
    guessed = False

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %d letters long.' %wordLength
    #print secretWord
    print '-------------'
    guessLeft = 8
    print 'You have %d guesses left.' %guessLeft
    available = string.ascii_lowercase
    print 'Available letters: ', available

    lettersGuessed = []

    while (guessLeft != 0 and guessed == False):

        lraw = raw_input('Please guess a letter: ')
        l = lraw.lower()

        while l not in available:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed)
            print '------------'
            print 'You have %d guesses left.' %guessLeft
            print 'Available letters: ', available
            lraw = raw_input('please guess a letter: ')
            l = lraw.lower()

        letter = [l]
        lettersGuessed += letter

        if l in secretWord:
            print 'Good guess: ', getGuessedWord(secretWord, lettersGuessed)
            print '------------'
            guessed = isWordGuessed(secretWord, lettersGuessed)

            if guessed == False:
                print 'You have %d guesses left.' %guessLeft
                available = getAvailableLetters(lettersGuessed)
                print 'Available letters: ', available
            else:
                print 'Congratulations, you won!'

        else:
            print 'Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed)
            print '------------'
            guessLeft -= 1
            if guessLeft != 0:
                print 'You have %d guesses left.' %guessLeft
                available = getAvailableLetters(lettersGuessed)
                print 'Available letters: ', available
            else:
                print 'Sorry, you ran out of guesses. The word was', secretWord,'.'