import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

def invr():
    return list(map(int, input().split()))

no = inp()
values = invr()
values.sort(reverse=True)

total = sum(values)
myShare = 0


for i in range(no):
    myShare+=values[i]
    if total // 2 < myShare:
        print(i+1)
        break 