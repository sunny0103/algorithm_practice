#6051. 정수 2개 입력받아 비교하기4
a, b = input().split()
print(int(a) != int(b))

#6052. 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

#6053. 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

#6054. 둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) & bool(int(b)))

#6055. 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#6056. 참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
print(bool(int(a))!= bool(int(b)))

#6057.  참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
print(bool(int(a)) == bool(int(b)))

#6058. 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
print((bool(int(a))==False) and (bool(int(b))==False))

#6059. 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

#6060. 비트단위로 AND 하여 출력하기
a, b = input().split()
a = int(a); b = int(b)
print(a&b)