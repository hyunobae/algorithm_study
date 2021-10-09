import sys

s = sys.stdin.readline()

temp = []
cnt = 0
p = 0
while True:
    if cnt >= len(s)-1:
        break

    if s[cnt] == '<':
        for c in s[cnt:]:
            if c == '>':
                temp.append(c)
                cnt += 1
                p = "".join(temp)
                print(p, end="")
                temp = []
                break

            else:
                temp.append(c)
                cnt += 1

    else:
        for c in s[cnt:]:
            if c == ' ' or c == '<' or c == '\n':
                temp.reverse()
                p = "".join(temp)
                print(p, end="")
                temp = []
                if c == ' ':
                    cnt += 1
                    print(' ', end='')
                break
            elif c == '\n':
                cnt += 1
            temp.append(c)
            cnt += 1
