import sys
input = sys.stdin.readline

def invr():
    return list(map(int, input().split()))

input1 = invr()
areaOFBoard = input1[0] * input1[1]
areaOfDominoes = 2

res = areaOFBoard // areaOfDominoes
print(res)