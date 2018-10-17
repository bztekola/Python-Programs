
astrng = 'akjndkjnfubnunjkj'
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #if aStr[(int(len(aStr))/2)] == char:
    #	return True
    #elif aStr[(int(len(aStr)/2))] > char:
    #	aStr[-1] = aStr[(int(len(aStr))/2)]
    #else:
    #	aStr[0] = aStr[(int(len(aStr))/2)]
    mid = int((len(aStr)//2))
    if aStr == '':
    	return False
    elif char == aStr[len(aStr)//2]:
    	return True
    elif len(aStr) == 1:
    	if aStr[0] == char:
    		return True
    	else:
    		return False
    else:
    	if char < aStr[mid]:
    		return isIn(char,aStr[:mid])
    	else:
    		return isIn(char,aStr[mid:])

print isIn('n', astrng)
