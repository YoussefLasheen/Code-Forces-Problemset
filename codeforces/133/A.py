import sys
input = sys.stdin.readline

def insr():
    s = input()
    return(list(s[:len(s) - 1]))

source = insr()
if any(x in source for x in ['H','Q','9']):
    print("YES")
else:
    print("NO")