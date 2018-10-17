s = 'azcbobobegghakl'
lngsubstr = 0
mtset = []
mtset1 = []

for i in range(len(s)):
	if s[i-1] <= s[i]:
		mtset += s[i]
	elif s[i-1] > s[i]:
		if len(mtset) > len(mtset1):
			mtset1 = mtset
			mtset = []
		else:
			mtset1 = mtset1

print(mtset1) 
s = 'azcbobobegghakl'
mtset = []
mtset1 = []

for i in range(len(s)):
	if s[i-1] <= s[i]:
		mtset += s[i-1]
	elif s[i-1] > s[i]:
		if len(mtset) > len(mtset1):
			mtset1 = mtset
			mtset = []
		else:
			mtset1 = mtset1