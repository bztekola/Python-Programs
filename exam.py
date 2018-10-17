'''dictionary = {0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0}'''
dictionary = {2: 0, 3: 3, 6: 1}
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
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
    listKeys = listKeys.sort()
    return(listKeys)
            
print(uniqueValues(dictionary))
    


