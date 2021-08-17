import sys

sys.setrecursionlimit(10 ** 6) #런타임에러(RecursionError)


def post(preorder, start, end):
    if start > end: # index가 역전되면 자신이 root다
        return

    root = preorder[start]
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root:
            break

        idx += 1

    post(preorder, start + 1, idx - 1) #왼쪽 서브트리
    post(preorder, idx, end) # 오른쪽 서브 트리 (root보다 값이 큰 tree)
    print(root)


preorder = []

while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

post(preorder, 0, len(preorder) - 1)
