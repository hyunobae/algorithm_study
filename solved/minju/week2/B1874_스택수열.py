N = int(input())

order = []
for i in range(N):
    order.append(int(input()))

stack = [0]
operator = ''
cnt = 0

for i, num in enumerate(order):
    while cnt < num:
        cnt += 1
        operator += '+'
        stack.append(cnt)

    if stack[-1] == num:
        operator += '-'
        stack.pop()

    else:
        operator = ['NO']
        break

for i in operator:
    print(i)
