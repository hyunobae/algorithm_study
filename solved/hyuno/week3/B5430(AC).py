import sys


def handle(oper, arr):
    flip = True
    if oper.count('D') > len(arr): #문제를 잘 읽자. RR이 연속으로 나오는 건 괜찮다. 여기서 한시간 날림. 반성
        sys.stdout.write('error\n')

    else:
        oper = list(oper.replace('RR', ''))
        for i in range(len(oper)):
            if oper[i] == 'R':
                flip = not flip

            elif oper[i] == 'D':
                if flip:
                    arr.pop(0)
                else:
                    arr.pop()
        if flip:
            sys.stdout.write("[" + ','.join(arr) + ']\n')
        else:
            sys.stdout.write("[" + ','.join(arr[::-1]) + ']\n')


case = int(sys.stdin.readline())

for i in range(case):
    oper = sys.stdin.readline().rstrip()

    num = int(sys.stdin.readline())

    arr = sys.stdin.readline()[1:-2].split(',')  # [ ] 빼고, ,로 split
    if num == 0:
        arr = []
    handle(oper, arr)
