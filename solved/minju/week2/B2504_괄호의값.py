brackets = input()
stack = []

brackets = brackets.replace('()', '2')
brackets = brackets.replace('[]', '3')

for b in brackets:
    if b == ')':
        sum = 0
        while stack:
            n = stack.pop()
            if n == '(':
                break
            if type(n) == int:
                sum += n
        else:   # 올바른 괄호아닐 때
            break
        
        stack.append(2*sum)
        
    elif b == ']':
        sum = 0
        while stack:
            n = stack.pop()
            if n == '[':
                break
            if type(n) == int:
                sum += n
        else:   # 올바른 괄호아닐 때
            break
        
        stack.append(3*sum)
    
    elif b.isdigit():    
        stack.append(int(b))

    else:
        stack.append(b)

result = 0
while stack:
    n = stack.pop()
    if type(n) == int:
        result += n
    else:   # 올바른 괄호아닐 때
        result = 0
        break
print(result)
