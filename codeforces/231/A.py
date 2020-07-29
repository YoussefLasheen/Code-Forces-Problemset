import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

def invr():
    return list(map(int, input().split()))



no = inp()
sum = 0
for i in range(no):
    wrd = invr()
    knows = 0
    for n in range(3):
        if wrd[n] == 1:
            knows+=1
    else:
        if knows>1:
            sum+=1
else:
    print(str(sum))