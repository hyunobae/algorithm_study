import sys

n = int(sys.stdin.readline())

stairs = [0]*300

dp = [0]*300 # dp[1] = 첫번째 계단으로 오는 최댓값

for i in range(n):
    stairs[i] = int(sys.stdin.readline())

# 현재 계단(n)에 오는 방법은 두가지이다.
# 1. n-2번째 계단을 밟고, n으로 오는 방법
# 2. n-3번째 계단, n-1번쩨 계단 후 n으로 오는 방법

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1] # 자연수니까 무조건 두개 밟는게 큼
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2]) # 이를 참고해서 점화식 세우면 끝

for i in range(3, n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3] + stairs[i-1] +stairs[i])

print(dp[n-1])