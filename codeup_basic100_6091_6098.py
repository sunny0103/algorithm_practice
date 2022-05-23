# 6091. 함께 문제 푸는 날
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d+=1
print(d)

#6092. 이상한 출석 번호 부르기1
import numpy as np
n = int(input())
a = list(map(int,input().split()))
d = list(np.zeros(24))
for i in range(n):
    d[a[i]] +=1
for i in range(1,24):
    print(int(d[i]), end=' ')

#6093.  이상한 출석 번호 부르기2
n = int(input())
k = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(k[i], end=' ')

#6094. 이상한 출석 번호 부르기3
n = int(input())
k = list(map(int, input().split()))
print(min(k))

#6095. 바둑판에 흰 돌 놓기
n = int(input())
data = []
for i in range(n):
    k = list(map(int, input().split()))
    data.append(k)
go = [[0]* 19 for _ in range(19)]

for j in range(n):
    go[data[j][0]-1][data[j][1]-1] = 1

for i in range(19):
    for j in range(19):
        print(go[i][j], end=' ')
    print()

#6096. 바둑알 십자 뒤집기
d=[]
for i in range(19):
    d.append(list(map(int,input().split())))

n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(19):
        if d[j][int(y)-1] == 0:
            d[j][int(y)-1] =1
        else:
            d[j][int(y)-1]=0
        if d[int(x)-1][j] ==0:
            d[int(x)-1][j] =1
        else:
            d[int(x)-1][j]=0

for i in range(19):
    for j in range(19):
        print(d[i][j],end =' ')
    print()
    
#6097. 설탕과자 뽑기
#6098.