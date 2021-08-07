# 강민주 BOJ 1018 체스판다시칠하기 풀이

```python
def diffCal(row, start):
    diff = [0]*len(row)
    for i, e in enumerate(row):
        if i%2==0:
            if e!=start:
                diff[i]=1
        else:
            if e==start:
                diff[i]=1

    return diff


N, M = map(int, input().split())

board = []
diff1 = []  # start with B
diff2 = []  # start with W

for i in range(N):
    board.append(input())

    if i%2==0:
        diff1.append(diffCal(board[i], 'B'))
        diff2.append(diffCal(board[i], 'W'))

    else:
        diff1.append(diffCal(board[i], 'W'))
        diff2.append(diffCal(board[i], 'B'))

cnt1, cnt2 = 0, 0   # sum of each row in diff1 and diff2                    
diff1_cnt = []      # list of cnt1 in diff1
diff2_cnt = []      # list of cnt2 in diff2

for r in range(N-7):
    for l in range(M-7):
        for i in range(8):
            cnt1 += sum(diff1[r+i][l:l+8])
            cnt2 += sum(diff2[r+i][l:l+8])
        diff1_cnt.append(cnt1)
        diff2_cnt.append(cnt2)
        cnt1, cnt2 = 0, 0
```