import statistics as st
from scipy import stats


n = int(input())
numList = list(int(num) for num in input().strip().split())[:n]
print(st.mean(numList))
print(st.median(numList))
print(int(stats.mode(numList)[0]))