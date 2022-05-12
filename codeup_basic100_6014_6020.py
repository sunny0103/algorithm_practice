 # 6014. 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.
f = input()
print(f)
print(f)
print(f)

 # 6015. 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자
a, b = input().split()
print(a)
print(b)

# 6016. 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.
c1, c2 = input().split()
print(c2, c1)

# 6017. 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.
s = input()
print(s, s, s)

# 6018. 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
a, b = input().split(':')
print(a, b, sep=':')

# 6019. "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 6020. 주민번호 입력받아 형태 바꿔 출력하기
b, n = input().split('-')
print(b+n)

