import sys

n = int(sys.stdin.readline())

info = []
people = 0

for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    info.append(x)
    people += x[1]

info.sort()

mid = people // 2 #인구 절반 구하기

if people % 2 == 1:
    mid += 1

cnt = 0

for x, p in info: # 인구 절반인 마을에 설치
    cnt += p # 사람수 더하면서 count

    if cnt >= mid: #사람수가 mid와 같아지면 마을에 설치
        print(x)
        break
