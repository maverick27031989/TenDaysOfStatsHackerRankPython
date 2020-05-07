import statistics as st
import math as math

n = int(input())
numList = list(int(num) for num in input().strip().split())[:n]

listMean = st.mean(numList)
sqrdDistMeanList = []

for i in numList:
    xi = (i - listMean) * (i - listMean)
    sqrdDistMeanList.append(xi)

IterlistSum = sum(sqrdDistMeanList)
computedValue = IterlistSum / n
sqrtComputedValue = math.sqrt(computedValue)
print(round(sqrtComputedValue, 1))
