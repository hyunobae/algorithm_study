import sys

sys.setrecursionlimit(10 ** 9)


def dfs(start, tree, result):
    for n, w in tree[start]:
        if result[n] == 0:  # 자식 노드 들른적 없으면 현재가중치 + 다음 가중치
            result[n] = result[start] + w
            dfs(n, tree, result)  # 자식 노드에서 dfs


num = int(sys.stdin.readline())

tree = [[] for _ in range(num + 1)]

for i in range(num - 1):
    x, y, w = map(int, sys.stdin.readline().split())
    tree[x].append([y, w])
    tree[y].append([x, w])

fresult = [0 for _ in range(num + 1)]

dfs(1, tree, fresult)  # 전체 탐색
fresult[1] = 0  # 양방향 입력으로 제거해줌 -> 루트노드로 설정해줌

maxlen = 0
idx = 0

for i in range(len(fresult)):
    if maxlen < fresult[i]:
        idx = i
        maxlen = fresult[i]

result = [0 for _ in range(num + 1)]
dfs(idx, tree, result)
result[idx] = 0 # root node 설정

print(max(result))
