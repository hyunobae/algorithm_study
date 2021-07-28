# BOJ 2798 블랙잭 풀이

```python 
N, M = map(int, input().split())
num = map(int, input().split())
num = list(num)
num.sort()


add = 0
max_num = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            add = num[i] + num[j] + num[k]
            if add <= M:
                if add > max_num:
                    max_num = add

            else:
                k = N

print(max_num)
```
