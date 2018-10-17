#Secretnum.py

print("Please think of a number between 0 and 100!")
guess = 50
print ("Is your secret number " + str(guess) + "?")
x = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

while x is not "c":
	if x == "h":
    		guess += ((100 - guess)/2)
    		print ("Is your secret number" + str(guess) + "?")
	elif x == "l":
    		guess -= (guess/2)
    		print ("Is your secret number" + str(guess) + "?")
	elif x is not("h" or "l" or"c"):
    		print ("Sorry, I did not understand your input.")
    		print ("Is your secret number" + str(guess) + "?")
    

print ("Game over. Your secret number was:" +str(guess))