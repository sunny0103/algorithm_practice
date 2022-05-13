# 6081. 16진수 구구단 출력하기
n = int(input(),16)
for i in range(1,int('F',16)+1):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082. 3 6 9 게임의 왕이 되자
n = int(input())
for i in range(1,n+1):
    if (i%10 == 3)|(i%10 == 6)|(i%10 == 9):
        print('X', end=' ')
    else:
        print(i,end=' ')

# 6083.  빛 섞어 색 만들기
r, g, b = input().split()
count = 0
r = int(r); g = int(g); b = int(b)
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j , k)
            count+=1
print(count)

# 6084. 소리 파일 저장용량 계산하기
h , b, c, s = input().split()
h = int(h); b = int(b); c = int(c); s = int(s)
space = h*b*c*s
mb = space/8/1024/1024
print(format(mb, '.1f'),'MB')

# 6085. 그림 파일 저장용량 계산하기
w, h, b = input().split()
w= int(w); h=int(h); b=int(b)
space = w*h*b
mb = space/8/1024/1024
print(format(round(mb,4), '.2f'),'MB')

# 6086. 거기까지! 이제 그만~
n = int(input())
s = 0
i = 1
while True:
    if n <=s :
        print(s)
        break
    s+=i
    i+=1
    
# 6087. 3의 배수는 통과
n = int(input())
for i in range(n+1):
    if i%3 ==0:
        continue
    print(i, end=' ')

# 6088. 수 나열하기1
a, d, n = input().split()
a = int(a); d = int(d); n = int(n)
for i in range(1, n):
    a+=d
print(a)

# 6089.  수 나열하기2
a, r, n = input().split()
a = int(a); r=int(r); n=int(n)
for i in range(1,n):
    a*=r
print(a)

# 6090. 수 나열하기3
a, m, d, n = input().split()
a = int(a); m=int(m); d=int(d); n= int(n)
for i in range(1, n):
    a*=m
    a+=d
print(a)
