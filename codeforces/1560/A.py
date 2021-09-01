noOfOperations = int(input())
for x in range(noOfOperations):
    length = int(input())
    n = 0
    while(n < length):
        if n % 3 == 0 or str(n)[-1] == '3':
            length += 1
            n += 1
            flag = False
        else:
            n += 1
            continue
    print(length-1)
