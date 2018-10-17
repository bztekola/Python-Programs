eps = .01
balance = 320000
annualInterestRate = .2
monthlyInterestRate = (annualInterestRate/12)
lowerBound = (balance / 12)
upperBound = (balance * (1 + monthlyInterestRate)**12)/12
bal = balance
while abs(bal) > eps:
    guess = (upperBound - lowerBound)/2 + lowerBound
    bal = (balance - guess) * ((1 + monthlyInterestRate) ** 11) - (guess * (( ((1+monthlyInterestRate) ** 11) - 1) / monthlyInterestRate))
    if bal > eps:
        lowerBound = guess
    elif bal < -eps:
        upperBound = guess
    else:
		print("Lowest payment: " + str(round(guess, 2))