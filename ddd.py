

dictionary = {2: 0, 3: 3, 6: 1}
def uniqueValues(aDict):
    listKeys = []
    dictValues = {}
    for i in aDict.keys():
        dVal = aDict[i]
        if dVal not in dictValues:
            dictValues[dVal] = []
        dictValues[dVal].append(i)
    for i in dictValues.keys():
        if len(dictValues[i]) == 1:
            listKeys.append(dictValues[i][0])
    listKeys.sort()
    return(listKeys)

print(uniqueValues(dictionary))    