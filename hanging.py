

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            return True
        else:
            return False
            
print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))