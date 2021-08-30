import sys

n = int(sys.stdin.readline())

d = [0] * (n+1)#해당 날짜에 들어오는 수익
t, p = [], [] # 걸리는날, 수익

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

M = 0

for i in range(n):
    M = max(M, d[i])# 해당 들어오는 날의 수익 vs 전의 값
    if i+t[i] > n:# 오늘 일을 했을때 끝나는 날이 n보다 작아야 할 수 있음
        continue
    d[i+t[i]] = max(M + p[i], d[i+t[i]]) #현재시기까지의 금액+오늘 맡는 일의 수익 vs 나중에 정산 받는 날의 금액

print(max(d))
