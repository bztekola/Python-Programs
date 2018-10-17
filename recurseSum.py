sum = ()
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if len(range(N)) < 10:
    	sum = N
    	return(sum)
    else:
		sum = (N%10 + sumDigits(N//10))
		return(sum)

print(sumDigits(12))

