#A program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def newb(balance, annualInterestRate, monthlyPaymentRate):
	for i in range(12):
		newbalance = (balance-(balance*monthlyPaymentRate))
		balance = newbalance + ((annualInterestRate/12)*newbalance)
		print (balance)
		i += 1
	return round(balance,2)
			
print('Remaining balance: '+ str(newb(balance, annualInterestRate, monthlyPaymentRate)))

print (newb(484,.2,.04))
