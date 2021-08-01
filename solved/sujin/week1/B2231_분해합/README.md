# 이수진 BOJ 2231 분해합 풀이

```python
def decomposition(decomp):
    N = input()
    N = int(N)

    for i in range(1, N):
        temp = i
        k = i

        while temp != 0:
            k += temp % 10
            temp = int(temp / 10)

        if decomp[k] == 0:
            decomp[k] = i

    print(decomp[N])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decomp = []
    for i in range(1500000):
        decomp.insert(i, 0)
    decomposition(decomp)
```