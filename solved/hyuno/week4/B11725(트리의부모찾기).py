import sys
from _collections import deque


def findParent(tree, parent):
    q = deque() # list를 사용하면 pop(0)을 할때 O(n) time 소모
    q.append(1) # root에서부터 탐색한다.

    while q:
        node = q.popleft()  # root level에서부터 뽑음
        for i in tree[node]:  # node와 이어진 edge의 node를 가져와서
            if parent[i] == 0:  # 이어진 노드가 아직 방문하지 않은 node라면
                parent[i] = node  # node의 부모가 i이다.
                q.append(i)  # loop를 위해 add

    return parent


num = int(sys.stdin.readline())

tree = [[] for i in range(num + 1)]  # index 1부터 사용함
parent = [0 for i in range(num + 1)]

for i in range(num - 1):  # tree 특성
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

parent = findParent(tree, parent)

for i in parent[2:]:
    print(i)
