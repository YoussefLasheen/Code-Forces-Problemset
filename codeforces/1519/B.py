noOfTestCases = int(input())
for x in range(noOfTestCases):
    inputValue = list(map(int, input().strip().split()))[:3]
    if (inputValue[0]*inputValue[1])-1 == inputValue[2]:
        print("yes")
    else:
        print("no")


    
