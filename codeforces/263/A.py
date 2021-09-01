xAxis = None
yAxis = None


for m in range(5):
    numbers = list(map(int,input().strip().split()))[:5]
    for i in range(5):
        if numbers[i] == 1:
            xAxis = i
            yAxis = m

output = abs(xAxis - 2) + abs(yAxis - 2) 
print(output)