# BOJ 2231 분해합
```python
num = int(input())

max_num = 1000001
temp = result = 0
min_num = max_num

for i in range(1, max_num):
    temp = i
    result = temp

    while temp != 0:
        result += temp % 10
        temp = temp / 10
        temp = int(temp)

    if result == num:
        print(i)
        break

    elif num == i:
        print(0)
```