def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a < b:
        result = a
        while result >= 1:
            if b%result == 0 and a%result == 0:
                return result
            else:
                result -= 1
    elif b < a:
        result = b
        while result >= 1:
            if b%result == 0 and a%result == 0:
                return result
            else:
                result -= 1
    else:
        return a 
    

print gcdIter(80, 80)

