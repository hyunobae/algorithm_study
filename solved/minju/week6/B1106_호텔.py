import sys

C, N = map(int, sys.stdin.readline().split())

cost = []
ppl = []
for i in range(N):
    c, p = map(int, sys.stdin.readline().split())
    cost.append(c)
    ppl.append(p)

least = max(ppl)    # '적어도' -> C~C+least명 일 때 최솟값을 가진다. (cf1)
result = [0] + [sys.maxsize]*(C+least)    # result[0] = 0
for i in range(min(ppl), C+least):
    for c, p in zip(cost, ppl):
        result[i] = min(result[i-p]+c, result[i])

print(min(result[C:]))


''' cf1)
C명 이상인 경우에 가지는 최솟값을 찾아야한다.
C+least명 이상인 경우에는 [C, C+least)명일 때의 값에서 비용을 더하기 때문에
[C, C+least) 중 정답을 가지는 고객 수가 있다.
'''
