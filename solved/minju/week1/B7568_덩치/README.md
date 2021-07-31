# 강민주 BOJ 7568 덩치 풀이

```python
N = int(input())

xy = []
for i in range(N):
    xy.append(list(map(float, input().split())))

for i in xy:
    rank = 1
    for j in xy:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
```


## 틀린 코드
```python
N = int(input())

xy = []     # xy[i] = [weight, height, index, rank]
for i in range(N):
    xy.append(list(map(float, input().split())))
    xy[i].append(i)
    
xy.sort(reverse=True)

xy[0].append(1)
for i in range(1,N):
    if xy[i][0] == xy[i-1][0]:
        xy[i].append(xy[i-1][-1])
    elif xy[i][1] < xy[i-1][1]:
        xy[i].append(i+1)
    else:
        xy[i].append(xy[i-1][-1])

xy.sort(key=lambda x:x[2])
for e in xy[0:-1]:
    print(e[3], end=' ') # print rank
print(xy[-1][3], end='')
```
정렬해서 앞에거만 비교하면 안됨.. 반례: 몸무게는 작은데 키가 가장 클 경우 1등인데, 정렬해서 하면 1등 아니게 나옴