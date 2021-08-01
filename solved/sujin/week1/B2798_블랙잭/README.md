# 이수진 BOJ 2798 블랙잭 풀이

```python
def blackJack():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    max_sum = 0
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if cards[i] + cards[j] + cards[k] <= M:
                    max_sum = cards[i] + cards[j] + cards[k]
                if max_sum > result:
                    result = max_sum
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    blackJack()
```