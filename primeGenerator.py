def genPrimes():
    primeList = []
    i = 2
    while True:
        x = True
        for n in primeList:
            if i % n == 0:
                i += 1
                x = False
                break
        if x != False:
            next = i
            yield next
            primeList.append(i)
            i += 1