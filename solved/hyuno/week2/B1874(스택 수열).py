import sys


def push(stack, num, result):
    stack.append(num)
    result.append('+')


n = int(sys.stdin.readline())
arr = []
stack = []

for i in range(1, n + 1):
    arr.append(int(sys.stdin.readline()))
arr.insert(0, 0)
stack.append(0)

num = 0
cnt = 0
f = 0
maxnum = 0
result = []
flag = 0

for i in range(1, n + 1):
    num = arr[i]
    for j in range(maxnum + 1, num + 1):
        push(stack, j, result)
        cnt += 1

    if num == stack[cnt]:
        f = stack.pop()
        if maxnum < f:
            maxnum = f

        result.append('-')
        cnt -= 1

    elif num < stack[cnt]:  # 종료조건
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in range(len(result)):
        print(result[i])
