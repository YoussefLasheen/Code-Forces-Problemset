noOfTestCases = int(input())
for x in range(noOfTestCases):
    result = ''
    length = int(input())
    inputChars = input()
    for c in range(length):
        if inputChars[c] == 'U':
            result += 'D'
        if inputChars[c] == 'D':
            result += 'U'
        if inputChars[c] == 'R' or inputChars[c] == 'L':
            result += inputChars[c]

    print(result)
