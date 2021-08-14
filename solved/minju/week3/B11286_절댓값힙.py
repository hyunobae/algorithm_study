import heapq
import sys

N = int(sys.stdin.readline())    # input() 쓰면 시간 초과
heap = []

for i in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(n), n))


'''
# 직접 구현

import sys

def heap_insert(heap, n):
    heap.append(n)

    index = len(heap)-1
    parent_i = index // 2
    while parent_i >= 1:
        parent = heap[parent_i]
        
        if abs(parent) > abs(n) or (abs(parent) == abs(n) and n < 0):
            heap[parent_i] = n
            heap[index] = parent
            index //= 2
            parent_i //= 2
        else:
            break


def heap_delete(heap):  
    print(heap[1])
    heap[1] = heap[-1]
    cmp = heap.pop()

    child_i = 2
    while child_i <= len(heap)-1:
        if child_i+1 <= len(heap)-1:    # 오른쪽 자식 or 왼쪽 자식 선택
            left = heap[child_i]
            right = heap[child_i+1]
            if abs(left) > abs(right) or (abs(left) == abs(right) and right < 0):
                child_i += 1
    
        child = heap[child_i]
        
        if abs(child) <= abs(cmp):
            heap[child_i] = cmp
            heap[child_i//2] = child
            child_i *= 2
        else:
            break
    

N = int(sys.stdin.readline())
heap = [0]

for i in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(heap) == 1:    # empty heap
            print(0)
            continue
        heap_delete(heap)
    else:
        heap_insert(heap, n)
'''
