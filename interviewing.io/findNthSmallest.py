def getNSmallest(n, arrNum):

    setLarger = list()
    setLargerCount = 0
    setSmaller = list()
    setSmallerCount = 0
    startIndex = 0

    for index in range(1, len(arrNum)):
        if arrNum[index] < arrNum[startIndex]:
            setSmaller.append(arrNum[index])
            setSmallerCount += 1
        elif arrNum[index] > arrNum[startIndex]:
            setLarger.append(arrNum[index])
            setLargerCount += 1

    position = setSmallerCount + 1

    if position == n:
        return arrNum[startIndex]
    elif n > position:
        return getNSmallest(n-position, setLarger)
    elif n < position:
        return getNSmallest(n, setSmaller)

# (1,2,5,7,8,9,11,12,15,21)
nums = (9,2,5,7,1,11,15,12,21,8)
print(getNSmallest(8, nums))
