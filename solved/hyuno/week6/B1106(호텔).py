import sys

C, N = map(int, sys.stdin.readline().split())

arr = []
dp = [0]+[100000]*(C+100) # n명 유치하는데 드는 비용 100000 -> 최대 100원* 1000명 유치

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))


for cs, peo in arr:
    for i in range(peo, C+101):#c는 적어도이기 때문에 각 도시 당 최대 유치 가능인 100명 경우까지 탐색해야함
        dp[i] = min(dp[i], dp[i-peo]+cs)# n명 유치하는 비용 vs (n명 유치 비용 - 현재 도시 인원수) + 홍보 비용 -> 직관적이지 않다

print(min(dp[C:C+101]))# C명 유치부터 100명까지 탐색


