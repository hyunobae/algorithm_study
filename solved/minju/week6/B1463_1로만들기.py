import sys

X = int(sys.stdin.readline())
cnt = [0]*(X+1)

for i in range(X, 1, -1):
    if i%3 == 0:
        cnt[i//3] = min(cnt[i]+1, cnt[i//3] if cnt[i//3]>0 else X+1)
    if i%2 == 0:
        cnt[i//2] = min(cnt[i]+1, cnt[i//2] if cnt[i//2]>0 else X+1)
    cnt[i-1] = min(cnt[i]+1, cnt[i-1] if cnt[i-1]>0 else X+1)

print(cnt[1])
