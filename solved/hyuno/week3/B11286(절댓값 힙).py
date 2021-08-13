import sys
import heapq

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    number = int(sys.stdin.readline())
    if number != 0:
        heapq.heappush(arr, (abs(number), number))  # heapq는 tuple의 앞 원소로 sorting

    elif number == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])

# num = int(sys.stdin.readline())
# arr = []
#
# for i in range(num):
#     number = int(sys.stdin.readline())
#     if number != 0:
#         arr.append((number, abs(number)))
#
#     elif number == 0:
#         if len(arr)==0:
#             print(0)
#         else:
#             arr.sort(key=lambda x: x[0])
#             print(arr[0][0])
#             arr.pop(0)

# timeout
# def cal(arr, absarr):
#     if len(arr) == 0:
#         print(0)
#
#     else:
#         minnum = min(absarr) #가장 작은 절댓값
#         mlist = list(filter(lambda x: absarr[x] == minnum, range(len(absarr))))  # 절대값이 가장 작은 index의 위치
#
#         temp = arr[0]
#         idx = 0
#         for i in mlist:
#             if arr[i] < temp:
#                 idx = arr.index(arr[i])
#                 temp = arr[i]
#                 break
#
#         print(temp)
#         arr.pop(idx)
#         absarr.pop(idx)
#
#
# num = int(sys.stdin.readline())
# arr = []
# absarr = []
# for i in range(num):
#     number = int(sys.stdin.readline())
#     if number != 0:
#         arr.append(number)
#         absarr.append(abs(number))
#
#     elif number == 0:
#         cal(arr, absarr)
