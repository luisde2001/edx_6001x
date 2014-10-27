def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            s += '_ '
        else:
            s += secretWord[i] + ' '
    return s