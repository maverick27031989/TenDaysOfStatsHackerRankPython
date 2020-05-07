n = int(input())
numListFirst = list(int(num) for num in input().strip().split())[:n]
numListSecond = list(int(num) for num in input().strip().split())[:n]

lst = []

for i in range(0, n):
    val = numListFirst[i] * numListSecond[i]
    lst.append(val)

upperValue = sum(lst)
lowerValue = sum(numListSecond)

finalValue = upperValue/lowerValue
print(round(finalValue, 1))