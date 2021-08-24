import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

totalsum = sum(arr) * 2 # 벌자리까지 일단 포함해서 더함

# 통은 양 끝에 있거나 벌 사이에 있어야 한다면 가장 꿀이 많은 곳에 통이 있어야 2번 더해져서 클 것이다
# 벌 통 벌 / 벌 벌 통 (거꾸로도 해야함)

answer = []

# 벌벌 통
bee2 = 1 #bee1은 0 고정
result = totalsum - arr[0]*2 - arr[bee2]*2
temp = result

bee2 += 1
while bee2 < n-1: #통이 우측 끝에 있다
    temp = temp + arr[bee2-1] - arr[bee2]*2 #bee2-1은 bee1이 오면서 가져오고, bee2의 자리는 빼줘여한다.
    result = max(result, temp)
    bee2 += 1

answer.append(result)

bee2 = n-2 # bee1은 n-1 고정
result = totalsum - arr[n-1]*2 - arr[bee2]*2
temp = result

bee2 -= 1
while bee2 > 0:
    temp = temp + arr[bee2+1] - arr[bee2]*2
    result = max(result, temp)
    bee2 -= 1

answer.append(result)

#벌 통 벌
honey = 0
for i in range(1, n-1):
    honey = max(honey, arr[i])

result = int(totalsum/2) -arr[0] - arr[n-1] + honey #honey는 이미 한번 포함되어 있어서 한번만 더 더해준다

answer.append(result)
print(max(answer))