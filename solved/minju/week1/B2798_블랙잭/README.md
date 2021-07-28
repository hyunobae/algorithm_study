# 강민주 BOJ 2798 블랙잭 풀이

```python
N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            card_sum = cards[i]+cards[j]+cards[k]
            if card_sum <= M and result<card_sum:
                result = card_sum

print(result)
```