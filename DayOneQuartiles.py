import statistics as st

n = int(input())

numList = list(int(num) for num in input().strip().split())[:n]

numList.sort()

medValue = st.median(numList)

lowerHalf = []
upperHalf = []

for i in numList:
    if i < medValue:
        lowerHalf.append(i)


for j in numList:
    if j > medValue:
        upperHalf.append(j)

print(int(st.median(lowerHalf)))
print(int(medValue))
print(int(st.median(upperHalf)))


#9
#3 7 8 5 12 14 21 13 18