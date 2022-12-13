
baseArray = str(open("input.txt", "r").read()).split("\n\n")

def a(baseArray):
    total = 0
    for value in baseArray:
        subArray= value.split("\n")
        tempTotal = 0
        for number in subArray:
            tempTotal+= int(number)
        if tempTotal > total:
            total = tempTotal
    print(total)


def b(baseArray):
    totalArr = []
    for value in baseArray:
        subArray= value.split("\n")
        tempTotal = 0
        for number in subArray:
            tempTotal+= int(number)
        totalArr.append(tempTotal)
    sortedArr = sorted(totalArr, reverse=True)
    print(sortedArr[0]+sortedArr[1]+sortedArr[2])

a(baseArray)
b(baseArray)