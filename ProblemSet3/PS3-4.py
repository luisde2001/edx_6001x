def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters = string.ascii_lowercase
    s = ''
    for i in range(len(availableLetters)):
        if availableLetters[i] not in lettersGuessed:
            s += availableLetters[i]
    return s