import sys
input = sys.stdin.readline


def invr():
    return list(map(int, input().split()))

input1 = invr()
input2 = invr()

no = input1[0]
place = input1[1]

output = 0

for i in range(no):
    if input2[i] <= 0:
        continue
    elif input2[i] >= input2[place-1]:
        output+=1
else:
    print(output)