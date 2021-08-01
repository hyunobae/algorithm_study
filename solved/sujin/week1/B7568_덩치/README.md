# 이수진 BOJ 7568 덩치 풀이

```python
def priority():
    N = int(input())

    people = []
    for _ in range(N):
        w, h = map(int, input().split())
        people.append((w, h))

    for i in people:
        rank = 1

        for j in people:
            if (i[0] != j[0]) & (i[1] != j[1]):
                if (i[0] < j[0]) & (i[1] < j[1]):
                    rank += 1

        print(rank, end=" ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    priority()
```