import sys

def check(arr):
    stack = []
    flag = True
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '[':
            stack.append(arr[i])

        else:
            if arr[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False

            elif arr[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()

                else:
                    flag = False

    if not stack and flag:  # stack이 비었고, flag가 true인 경우(올바른 괄호일때)
        return True

    else:
        return False


arr = list(sys.stdin.readline().strip())

stack = []

chk = check(arr)

if chk:
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '[':
            stack.append(arr[i])

        elif arr[i] == ')' and stack:
            if stack[-1] == '(':
                stack[-1] = 2  # ()여서 2로 저장해줌

            else:  # 숫자인 경우 -> 숫자 전 괄호가 나오기 전까지 계산해준다
                temp = 0
                for j in range(len(stack) - 1, -1, -1):  # stack의 끝부터 0까지 한칸씩 오며 탐색
                    if stack[j] == '(':
                        stack[-1] = temp * 2  # (를 pop하고 숫자 저장
                        break

                    else:
                        temp += stack[-1]
                        stack.pop()


        elif arr[i] == ']' and stack:
            if stack[-1] == '[':
                stack[-1] = 3  # []여서 3으로 저장해줌

            else:  # 숫자인 경우 -> 숫자 전 괄호가 나오기 전까지 계산해준다
                temp = 0
                for j in range(len(stack) - 1, -1, -1):  # stack의 끝부터 0까지 한칸씩 오며 탐색
                    if stack[j] == '[':
                        stack[-1] = temp * 3  # [를 pop하고 숫자 저장
                        break

                    else:
                        temp += stack[-1]
                        stack.pop()

    print(sum(stack))


else:
    print(0)
