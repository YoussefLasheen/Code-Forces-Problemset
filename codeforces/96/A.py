import sys
input = sys.stdin.readline


def insr():
    s = input()
    return(list(s[:len(s) - 1]))

input1 = insr()

for i in range(len(input1)):
    repeating = 0
    for m in range(i,len(input1)):
        if input1[i] == input1[m]:
            repeating+=1
        else:
            break
    if repeating >=7:
        print("YES")
        break
else:
    print("NO")