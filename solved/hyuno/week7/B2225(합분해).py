import sys

# 0부터 N까지의 정수 K개를 더해서 N이 되는 경우의 수
# 덧셈 순서는 다른 경우임
# N, K가 4, 3인 경우까지만 그려보면 점화식을 찾을 수 있다.
# dp[i][j] = dp[i][j-1] + dp[i-1][j]이다.
N, K = map(int, input().split())

dp = [[0]*201 for i in range(201)]

for i in range(201):
    dp[1][i] = 1 # 자기자신만 가지는 경우
    dp[2][i] = i+1 # 자리 바꾼 값*2 + 1/2 값의 합

    if i>=2:
        dp[i][1] = i # k개로 1을 표현하는 방법은 k개다

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K][N]%1000000000)



