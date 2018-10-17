balance = 3329
annualInterestRate = 0.2
minimumMonthlyPayment = 10
#This program figures out the lowest monthly payment (divisible by 10) that should be paid in order to 
#eliminate a specific debt with a certain annual interest rate

def payDebt(balance, annualInterestRate, minimumMonthlyPayment):
	bal = balance
	for i in range(12):
		newbalance = bal - minimumMonthlyPayment
		newb = newbalance + ((annualInterestRate/12)*newbalance)
		bal = newb
	if bal > 0:
		minimumMonthlyPayment += 10
		return payDebt(balance, annualInterestRate, minimumMonthlyPayment)
	else:
		return minimumMonthlyPayment

print("Lowest payment: " + str(payDebt(balance, annualInterestRate, minimumMonthlyPayment)))
