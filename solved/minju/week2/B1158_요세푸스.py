N, K = list(map(int, input().split()))

people = list(range(1, N+1))
index = 0

print('<', end='')
for i in range(N-1):
    index = (index + K-1) % len(people)
    print(people[index], end='')
    print(',', end=' ')
    del people[index]

print(people[0], end='')
print('>')
