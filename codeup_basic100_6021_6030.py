# 6021. 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
#입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
s = input()
for i in range(len(s)):
    print(s[i])

# 6022. 연월일 입력받아 나누어 출력하기
s = input()
print(s[:2], s[2:4], s[4:])

# 6023. 시분초 입력받아 분만 출력하기
h, m, s = input().split(':')
print(m)

# 6024. 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()
s = w1+w2
print(s)

# 6025. 정수 2개 입력받아 합 계산하기
a, b = input().split()
c = int(a)+int(b)
print(c)

# 6026. 실수 2개 입력받아 합 계산하기
f1 = input()
f2 = input()
f = float(f1)+float(f2)
print(f)

# x: hexa o: octagonal

# 6027. 10진 정수 입력받아 16진수로 출력하기1
a = int(input())
print('%x'%a) # 소문자로 출력 

# 6028. 10진 정수 입력받아 16진수로 출력하기2
a = int(input())
print('%X'%a)  # 대문자로 출력

# 6029.16진 정수 입력받아 8진수로 출력하기
h = int(input(), 16) # 16 진수로 입력 받음
print('%o'%h)

# 6030.영문자 1개 입력받아 10진수로 변환하기
# ord():문자를 10진수로 변환한값
n = ord(input())
print(n)