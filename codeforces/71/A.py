import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

def insr():
    s = input()
    return(s[:len(s) - 1])



no = inp()

for i in range(no):
    wrd = insr()
    if len(wrd) > 10:
        print(wrd[0]+str(len(wrd)-2)+wrd[-1])
    else:
        print(wrd)