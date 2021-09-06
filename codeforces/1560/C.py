import math
testCases = int(input())
for a in range(testCases):
    cellNumber = int(input())
    local = 0
    
    sideLength = 0
    numberLeft = cellNumber
    for i in range(int(math.sqrt(cellNumber)),-1,-1):
      if cellNumber - i**2 >0:
        local= i**2
        sideLength = i+1
        break
    numberLeft -= local
    def calculatePosition():
      pos = [0,0]
      if numberLeft <= sideLength:
        pos[1] = str(sideLength)
        pos[0] = str(numberLeft)
      else:
        pos[1] = str(sideLength - (numberLeft - sideLength))
        pos[0] = str(sideLength)
      return ' '.join(pos)
    print(calculatePosition())