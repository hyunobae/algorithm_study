# BOJ 7568 덩치 풀이

```python 
num = int(input())
person = []
grade=[]

for i in range(num):
    w, h = map(int, input().split())
    person.append((w, h))
    grade.append(1)

for i in range(num-1):
    for j in range(i+1, num):
        if (person[i][0] > person[j][0]) & (person[i][1] > person[j][1]):
            grade[j] += 1

        elif (person[i][0] < person[j][0]) & (person[i][1] < person[j][1]):
            grade[i] += 1

for i in range(num):
    print(str(grade[i]) + ' ' , end='')

```