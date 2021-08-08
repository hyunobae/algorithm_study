import sys

case = int(sys.stdin.readline())

def queue(prior, idx):  # idx: 몇번째로 인쇄되는지 궁금한 index
    loop = 0

    save = [0 for i in range(len(prior))]
    save[idx] = 1

    while (True):
        temp = prior[0]
        if max(prior) == temp:
            loop += 1
            if save[0] == 1: #내가 찾는 문서인 경우
                print(loop) # 몇번째로 pop 되는지 확인
                break

            else:
                prior.pop(0)
                save.pop(0)

        else:
            t = prior.pop(0)
            f = save.pop(0)
            prior.append(t)
            save.append(f)


for i in range(case):
    cnt, idx = map(int, sys.stdin.readline().split())
    prior = list(map(int, sys.stdin.readline().split()))
    queue(prior, idx)
