from itertools import combinations
 
 
testCases = int(input())
for a in range(testCases):
    input()
    y = input()
 
    def isPrime(n):
        if (n == 1):
            return False
        elif (n == 2):
            return True
        else:
            for x in range(2, n):
                if(n % x == 0):
                    return False
            return True
 
    result = y
 
    pCombinations = sum([list(map(list, combinations(y, i+1)))
                        for i in range(2)], [])

    for i in pCombinations:
        local = ''.join(i)
 
        if len(local) < len(result) and not isPrime(int(local)):
            result = local
    print(len(result))
    print(result)
    
