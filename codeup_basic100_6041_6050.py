# 6041. 정수 2개 입력받아 나눈 몫 계산하기
a, b = input().split()
c  = int(a)%int(b)
print(c)

# 6042.실수 1개 입력받아 소숫점이하 자리 변환하기
fc = float(input())
print(format(fc,'.2f'))

# 6043.실수 2개 입력받아 나눈 결과 계산하기
f1, f2 = input().split()
ff = round(float(f1)/float(f2), 4)
print(format(ff, '.3f'))

# 6044. 정수 2개 입력받아 자동 계산하기
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,'.2f'))

# 6045. 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
a = int(a); b = int(b); c = int(c)
s  = a+b+c
print(s, format(round(s/3, 3),'.2f'))

# 6046. 정수 1개 입력받아 2배 곱해 출력하기
a = input()
a  = int(a)
print(a<<1)

# 6047. 2의 거듭제곱 배로 곱해 출력하기
a, b = input().split()
a = int(a); b = int(b)
print(a<<b)

# 6048. 정수 2개 입력받아 비교하기1
a, b = input().split()
print(int(a)< int(b))

# 6049.  정수 2개 입력받아 비교하기2
a, b = input().split()
print(int(a) == int(b))

# 6050.  정수 2개 입력받아 비교하기3
a, b = input().split()
print(int(a) <= int(b))