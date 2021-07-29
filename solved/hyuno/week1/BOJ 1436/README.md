# BOJ 1436 영화감독 숌 풀이

```python 
num = int(input())
cnt = 0
number = 666

while True:
    if '666' in str(number):
        cnt += 1

    if num == cnt:
        print(number)
        break

    number += 1

```
***
### Comment
처음에 1부터 10000까지 입력된다해서 for문으로 풀려고 했지만 문제에서 666 -> 1이 되기 때문에
for(1, 10001)로 loop를 돌리게 되면 비교대상이 달라서 틀린다. 따라서, while이 합리적이었다.