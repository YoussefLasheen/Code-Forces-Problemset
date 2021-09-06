
testCases = int(input())
for a in range(testCases):
    y = int(input())
    result = y // 10
    if str(y)[-1] == '9':
      print(result+1)
      continue
    
    print(result)