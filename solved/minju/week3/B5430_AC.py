import sys

T = int(sys.stdin.readline())

for i in range(T):
    func = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    array = sys.stdin.readline().rstrip()[1:-1].split(',')    # 개행문자까지 입력
    if array[0] == '':
        array = []
    
    reverse = False 
    for f in func:
        if f == 'R':
            reverse = not reverse
        else:    # 'D'
            if len(array) == 0:
                print('error')
                break
            
            if reverse:
                array.pop()
            else:
                array.pop(0)
    else:
        if reverse:
            array.reverse()
            # join(array.reverse()) 하면 안됨. reverse return값 None
            print('[' + ','.join(array) + ']')
        else:
            print('[' + ','.join(array) + ']')
