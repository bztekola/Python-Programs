

s = "andbobobsdjybobaaabob"
numbob = 0
x = "bob"

for i in range(len(s)):
	if x == s[i:i+3]:
		numbob += 1
print ("Number of times bob occurs is: " + str(numbob)) 

