# BOJ 1018 체스판 다시 칠하기 풀이

```python 
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

rloop = N - 8 + 1
cloop = M - 8 + 1
strtB = 0
strtW = 0

result = []

for o in range(rloop):
    for i in range(cloop):
        strtB = 0
        strtW = 0
        for j in range(o, 8 + o):
            for k in range(i, 8 + i):
                if (j + k) % 2 == 0: # 좌표의 합이 짝, 홀
                    if board[j][k] != 'W': # W로 시작했는데 W가 아닌 경우
                        strtW += 1
                    if board[j][k] != 'B':# B로 시
                        strtB += 1

                else:
                    if board[j][k] != 'B': #W로 시작했는데 바로 밑에 W가 오는 경우
                        strtW += 1

                    if board[j][k] != 'W': #B로 시작
                        strtB += 1

        result.append(strtB)
        result.append(strtW)

print(min(result))

```

***
# 하드 코딩 실패
``` python
for o in range(rloop):
    for i in range(cloop):
        strtB = 0
        strtW = 0
        for j in range(o, 8 + o):
            for k in range(i, 8 + i):
                if board[o][i] == 'B':  # 처음에 B로 시작하는 경우
                    if (j % 2 == 0 and k % 2 == 0) or (j % 2 == 1 and k % 2 == 1):
                        if board[j][k] == 'W':
                            strtB += 1

                    if (j % 2 == 0 and k % 2 == 1) or (j % 2 == 1 and k % 2 == 0):  # 0,1 2,1 ..
                        if board[j][k] == 'B':
                            strtB += 1

                elif board[o][i] == 'W':
                    if (j % 2 == 0 and k % 2 == 0) or (j % 2 == 1 and k % 2 == 1):
                        if board[j][k] == 'B':
                            strtW += 1

                    if (j % 2 == 0 and k % 2 == 1) or (j % 2 == 1 and k % 2 == 0):  # 짝수행의 홀수열 체
                        if board[j][k] == 'W':
                            strtW += 1
```