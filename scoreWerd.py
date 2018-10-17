aDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 }
test = "testString"
def add(first, second):
  return first + second
def score(word, f):
  letter1 = 0
  letter2 = 0
  for i in range(0, len(word)):
    s = i * aDict[word[i].lower()]
    if s > letter1:
      letter2 = letter1
      letter1 = s
    elif s > letter2:
      letter2 = s
      
  return add(letter1, letter2)
print score(test, add)

