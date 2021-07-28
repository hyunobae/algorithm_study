# 강민주 BOJ 2231 분해합 풀이

```python
N = input()

max_digitsum = int(N[0])-1 + 9*(len(N)-1)	# find max digitsum
N = int(N)

for num in range(N-max_digitsum, N):
    sum_digit = sum(map(int, str(num)))	# digit sum
    if sum_digit+num == N:
        print(num)
        break
else: print(0)    
```