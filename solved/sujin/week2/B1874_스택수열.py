n = int(input())
count = 0
stack = []
op = []
temp = True

for i in range(0,n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      op.append("+")

    if stack[-1]==x:
        stack.pop()
        op.append("-")
    else:
        temp = False


if temp==False:
    print("NO")
else:
    print("\n".join(op))

