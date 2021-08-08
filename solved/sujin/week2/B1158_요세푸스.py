N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]

result= []   # 제거된 사람
index = 0  # 제거될 사람의 인덱스

for i in range(N):
    index += K-1
    if index >= len(arr):
        index = index%len(arr)

    result.append(str(arr.pop(index)))
print("<",", ".join(result)[:],">", sep='')