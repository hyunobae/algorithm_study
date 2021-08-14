import sys

N = int(sys.stdin.readline())
curr = 0

for i in range(N):
    size, index = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))

    result = 0
    while True:
        curr = priority.pop(0)
        
        for j in priority:
            if curr < j:
                priority.append(curr)
                break
        else:
            result += 1
            if index == 0:
                print(result)
                break
            
        if index == 0:
                index = len(priority)-1
        else:
            index -= 1
