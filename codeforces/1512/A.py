


noOfOperations = int(input())

for x in range(noOfOperations):
    noOfElements = int(input())
    numbers = list(map(int,input().strip().split()))[:noOfElements]
    #print (numbers)
    currentNo = numbers[0]
    c=False

    if numbers[0]!=numbers[1]:
        if numbers[0]!=numbers[2]:
            print(1)
        else:
            print(2)
    elif numbers[-1]!=numbers[-2]:
        if numbers[-1]!=numbers[-3]:
            print(noOfElements)
        else:
            print(noOfElements-1)
    else:
        for y in range(len(numbers)):
            if numbers[y]!=currentNo:
                if c==True:
                    print(y)
                    break
                else:
                    c=True
            currentNo = numbers[y]