import sys

T = []
P = []

# 입력 받기
N = int(sys.stdin.readline())
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

profit = [0]*(N+1)    # index일 까지의 금액을 담는 list

for i in range(0, N):
    if i + T[i] <= N:   # N일 초과하는 상담은 불가
        # 이 상담을 수행했을 때의 금액과 이전에 구한 금액을 비교
        profit[i+T[i]] = max(profit[i]+P[i], profit[i+T[i]]) 

    profit[i+1] = max(profit[i+1], profit[i])    # 다음 날짜 업데이트

print(profit[N])
