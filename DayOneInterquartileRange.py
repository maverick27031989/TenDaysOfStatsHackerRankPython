import statistics as st

n = int(input())
ele = list(int(num) for num in input().strip().split())[:n]
freq = list(int(num) for num in input().strip().split())[:n]

lst = []

for i in range(n):
    lst += [ele[i]] * freq[i]

lst.sort()

medValue = st.median(lst)

lowerHalf = []
upperHalf = []

for i in lst:
    if i < medValue:
        lowerHalf.append(i)


for j in lst:
    if j > medValue:
        upperHalf.append(j)

medLowerValue = st.median(lowerHalf)
medUpperValue = st.median(upperHalf)

intquarRange = medUpperValue - medLowerValue

print(intquarRange)
#6
#6 12 8 10 20 16
#5 4 3 2 1 5