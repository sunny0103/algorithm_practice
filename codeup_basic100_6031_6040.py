# 6031. 정수 입력받아 유니코드 문자로 변환하기
c  = int(input())
print(chr(c))

# 6032. 정수 1개 입력받아 부호 바꾸기
i = int(input())
print(-i)

# 6033. 문자 1개 입력받아 다음 문자 출력하기
c = ord(input())
print(chr(c+1))

# 6034. 정수 2개 입력받아 차 계산하기
a, b = input().split()
c = int(a) - int(b)
print(c)

# 6035. 실수 2개 입력받아 곱 계산하기
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

# 6036. 단어 여러 번 출력하기
w, n = input().split()
print(w*int(n))

# 6037. 문장 여러 번 출력하기
n = input()
s = input()
print(int(n)*s)

# 6038. 정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
c = int(a)**int(b)
print(c)

# 6039. 실수 2개 입력받아 거듭제곱 계산하기
f1, f2 = input().split()
f = float(f1)**float(f2)
print(f)

# 6040. 정수 2개 입력받아 나눈 몫 계산하기
a, b = input().split()
print(int(a)//int(b))