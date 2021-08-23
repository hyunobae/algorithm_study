import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

cnt = 2

result = 0
for i in range(num):
    if cnt == i:
        cnt += 3
        continue

    result += arr[i]

print(result)

