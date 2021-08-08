N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]

pop = []

pop_idx = K - 1
cur = pop_idx # pop할 사람 index

while True:
    pop.append(arr.pop(cur))

    if len(arr)==0:
        break

    cur = (cur + pop_idx) % len(arr) # 6 % 5 =1

print('<', end='')
for i in range(len(pop)):
    if i == len(pop)-1:
        print(str(pop[i])+'>', end='')
    else:
        print(str(pop[i])+', ', end='')
