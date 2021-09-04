noOfTestCases = int(input())
for x in range(noOfTestCases):
    input()

    startCell = list(map(int, input().strip().split()))[:2]
    finishCell = list(map(int, input().strip().split()))[:2]
    forbiddenCell = list(map(int, input().strip().split()))[:2]

    distance = 0

    def onSameUnitVector(a,b):
        if a[0]==b[0] or a[1]==b[1]:
            return True

    def cBetween():
        if startCell[0]>forbiddenCell[0]>finishCell[0] or startCell[1]>forbiddenCell[1]>finishCell[1] or startCell[0]<forbiddenCell[0]<finishCell[0] or startCell[1]<forbiddenCell[1]<finishCell[1]:
            return True
        else:
            return False

    def calculateDistance():
        xDistance = abs(startCell[0]-finishCell[0])
        yDistance = abs(startCell[1]-finishCell[1])
        return xDistance + yDistance

    if not onSameUnitVector(startCell,finishCell):
        distance = calculateDistance()
    elif (onSameUnitVector(startCell,forbiddenCell) or onSameUnitVector(finishCell,forbiddenCell)) and cBetween():
        distance = calculateDistance() + 2
    else:
        distance = calculateDistance()


    print(distance)