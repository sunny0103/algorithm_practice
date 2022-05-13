# 6071.  0 입력될 때까지 무한 출력하기
n=1
while n!=0:
    n = int(input())
    if n!=0:
        print(n)

# 6072. 정수 1개 입력받아 카운트다운 출력하기1
n = int(input())

while n!=0:
    print(n)
    n -=1

# 6073. 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())

while n!=0:
    n-=1
    print(n)

# 6074. 문자 1개 입력받아 알파벳 출력하기
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end=' ')
    t += 1

# 6075. 정수 1개 입력받아 그 수까지 출력하기1
n = int(input())
i = 0
while i <= n:
    print(i)
    i += 1 

# 6076. 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())
for i in range(n+1):
    print(i)

# 6077. 짝수 합 구하기
n = int(input())
s = 0
for i in range(n+1):
    if i%2==0:
        s+=i
print(s)

# 6078. 원하는 문자가 입력될 때까지 반복 출력하기
while True:
    ch = input()
    print(ch)
    if ch =='q':
        break

# 6079. 언제까지 더해야 할까?
n = int(input())
s = 0
i = 1
while True:
    s += i
    if n <= s:
        print(i)
        break
    i+=1

# 6080. 주사위 2개 던지기
n, m = input().split()
n = int(n); m = int(m)
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)