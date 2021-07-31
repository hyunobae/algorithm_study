# 강민주 BOJ 1436 영화감독숌 풀이

## 코드1
```python
N = int(input())

fnum = 0    # front number. there are three digits after fnum
cnt = N
result = 0

while cnt>0:
    s_fnum = str(fnum)
    
    while s_fnum[-1] != '6':
        cnt -= 1
        if cnt==0:
            print(int(s_fnum+'666'))
            break
   
        fnum += 1
        s_fnum = str(fnum)
                    
    if s_fnum[-1] == '6':
        six_cnt = 1
        len_fnum = len(s_fnum)

        # count '6' in a row
        for i in range(len_fnum-1):
            if s_fnum[len_fnum-2-i] == '6':
                six_cnt += 1
            else: break

        if six_cnt == 1:    # ex) 16___
            if cnt <= 10:
                print(s_fnum + '66' + str(cnt-1))
                cnt = 0
            else:
                cnt -= 10
                
        elif six_cnt == 2:  # ex) 66___
            if cnt <= 10:   # one digit
                print(s_fnum + '60' + str(cnt-1))
                cnt = 0
            elif cnt <= 100:    # two digits
                print(s_fnum + '6' + str(cnt-1))
                cnt = 0
            else:
                cnt -= 100

        else:   # ex) 1666___
            if cnt <= 10:   # one digit
                print(s_fnum + '00' + str(cnt-1))
                cnt = 0
            elif cnt <= 100:    # two digits
                print(s_fnum + '0' + str(cnt-1))
                cnt = 0
            elif cnt <= 1000:   # three digits
                print(s_fnum + str(cnt-1))
                cnt = 0
            else: cnt -= 1000

        fnum += 1
```
별짓을 다했네...


## 코드 2
```python
N = int(input())

num= 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1
    
```