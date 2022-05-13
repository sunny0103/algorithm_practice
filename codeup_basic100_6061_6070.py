# 6061. 비트단위로 OR 하여 출력하기
a, b = input().split()
print(int(a)|int(b))

# 6062. 비트단위로 XOR 하여 출력하기
a, b = input().split()
print(int(a)^int(b))

# 6063.정수 2개 입력받아 큰 값 출력하기
a, b = input().split()
a = int(a); b = int(b)
c = (a if a>b else b)
print(c)

# 6064. 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
a = int(a); b = int(b); c = int(c)
mn = (a if a<b else b) if((a if a<b else b)<c) else c
print(mn)

# 6065. 정수 3개 입력받아 짝수만 출력하기
a, b, c = input().split()
a = int(a); b = int(b); c = int(c)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

# 6066. 정수 3개 입력받아 짝/홀 출력하기
a, b, c = input().split()
for i in a,b,c:
    if int(i) % 2 ==0:
        print('even')
    else:
        print('odd') 

# 6067. 정수 1개 입력받아 분류하기
a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
else:
    if a%2==0:
        print('C')
    else:
        print('D')

# 6068. 점수 입력받아 평가 출력하기
n = int(input())

if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print('C')
else:
    print('D')

# 6069. 평가 입력받아 다르게 출력하기
word = input()

if word == 'A':
    print('best!!!')
elif word =='B':
    print('good!!')
elif word == 'C':
    print('run!')
elif word == 'D':
    print('slowly~')
else:
    print('what?')

# 6070. 월 입력받아 계절 출력하기
m = int(input())

if m//3 ==1:
    print('spring')
elif m//3 ==2:
    print('summer')
elif m//3 ==3:
    print('fall')
else:
    print('winter')