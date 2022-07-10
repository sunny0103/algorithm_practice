###백준 기초 알고리즘
## 수학
# 31
# 11653 소인수 분해
n= int(input())
i = 2
while n !=1:
    if n%i ==0:
        n/=i
        print(i)
    else:
        i+=1

# 32
# 11576 base conversion
import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
m = int(input())
li = list(map(int, input().rstrip().split()))
li.reverse()
result = 0 
for i in range(m):
    result+=(a**i)*li[i]

new = []
while result//b:
    new.append(result%b)
    result//=b
new.append(result)
new.reverse()
print(' '.join(map(str,new)))


# 33
# 2745 진법변환
import sys
input = sys.stdin.readline
nums, b = input().rstrip().split()
nums = ''.join(reversed(nums))
b = int(b)
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tens = 0 # 십진법 결과 저장
for i, n in enumerate(nums):
    tens+=(b**i)*number.index(n)
print(tens)

# 34
# 11005 진법변환2
import sys
input = sys.stdin.readline
n, b = map(int, input().rstrip().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=[]
while n//b:
    result.append(number[n%b])
    n//=b
result.append(number[n]) # 남은 최종 몫을 추가
result.reverse()
print(''.join(result))

# 35
# 1373 2진수 8진수
# 이하 시간초과
import sys
input = sys.stdin.readline

nums = input().rstrip()
nums =''.join(reversed(nums))
tens =0 # 10진수 초기화
for i, n in enumerate(nums):
    tens+=(2**i)*int(n)
result = []
while tens//8:
    result.append(tens%8)
    tens//=8
result.append(tens)
result.reverse()
print(''.join(map(str,result)))
# 내장함수 사용
# int(##, 2) 2진수를 10 진수로
# oct : octagon 8진수 표현 oct(##)[2:] 
print(oct(int(input(),2))[2:]) 

# 36 
# 1212 8진수 2진수
print(bin(int(input(),8))[2:])

# 37
# 2089 -2진수
# from https://skeo131.tistory.com/56

import sys
input = sys.stdin.readline

n = int(input())

def neg_base(n, k):
    if n==0:
        return '0'
    else:
        if n%2 == 0:
            return neg_base(n//k, k)+'0'
        else:
            return neg_base(n//k+1, k)+'1'

result = neg_base(n,-2)

if result == '0':
    print(result)
else:
    print(result[1:])

## 다이나믹 프로그래밍 1
# 38 
# 1463 1로 만들기
import sys
input = sys.stdin.readline
n= int(input())
array = [0]* (n+1)
for i in range(2,n+1):
    array[i] = array[i-1] +1
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2]+1)
    if i % 3 == 0:
        array[i] = min(array[i], array[i//3]+1)
print(array[n]) 

# 39
# 2225 합분해
import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

array =[[0]* 201 for _ in range(201)]
for i in range(201):
    array[1][i] =1
    array[2][i] = i+1

for j in range(3,201):
    array[j][1] = j
    for t in range(2, 201):
        array[j][t] = array[j][t-1] + array[j-1][t]

print(array[k][n])

# 40 
# 24416 피보나치 수열

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def fibonacci(n):
    fibo = [0]* (n+1)
    fibo[1] = 1
    fibo[2] = 2
    count = 0
    for i in range(3, n+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
        count+=1
    return count
n = int(input())
    
print(fib(n),fibonacci(n))







