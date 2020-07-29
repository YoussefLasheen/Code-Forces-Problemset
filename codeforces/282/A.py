import sys
input = sys.stdin.readline


def inp():
    return(int(input()))




input1 = inp()

res = 0

for i in range(input1):
    operation = input()
    if '++' in operation:
        res+=1
    elif '--' in operation:
        res-=1
else:
    print(res)