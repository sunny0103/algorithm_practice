### 백준 알고리즘 기초
# 21.
# 11656 점미사 배열
import sys
strings = sys.stdin.readline().rstrip()

li = []

for i in range(len(strings)):
    li.append(strings[i:])

li.sort()

for l in li:
    print(l)

## 수학1
# 22
# 10430 나머지
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 23
# 2609 최대공약수 최소 공배수
'''
최대공약수와 최소공배수의 관계
유클리드 호제법
a * b = gcd(a,b) * lcm(a, b)
gcd : greatest common divisor
ldm : least common multiple
'''
a, b = map(int, input().split())

def gcd(a,b):
    if a%b!=0:
        return gcd(b,a%b)
    else:
        return b

print(gcd(a, b))
print(int(a*b/gcd(a, b)))

# 24
# 1934 최소공배수

def gcd(a,b):
    if a%b!=0:
        return gcd(b,a%b)
    else:
        return b

def lcm (a,b):
    return a*b/gcd(a,b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(int(lcm(a,b)))

# 25
# 1929 소수 찾기
'''
1과 자기 자신을 제외한 약수가 존재하는지 확인하려면, 자신의 루트 값까지 확인하면 된다.
25의 경우 1과 25를 제외한 루트값이 5까지 확인하면 된다.
'''
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

m, n = map(int, input().split())

for i in range(m,n+1):
    if is_prime(i):
        print(i)

# 26
# 1978 소수찾기

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
li = list(map(int, input().split()))
result = 0
for j in li:
    if is_prime(j):
        result+=1
print(result)
    
# 27 
# 6588 골드바흐의 추측
'''
개념
1. n까지 주어졌을때 n까지 모든 소수 출력
2. (n-출력된 소수) 가 소수인지 확인
3. 오름차순 정렬
4. 중복제거
'''
# https://wikidocs.net/21638
# https://velog.io/@gyuseok-dev/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

# 28
# 10872 팩토리얼

def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

n = int(input())

s = str(factorial(n))
count = 0
for i in range(len(s)-1,-1,-1):
    if s[i]=='0':
        count+=1
    else:
        break
print(count)

# 29
# 2004 조합0의갯수
# https://deok2kim.tistory.com/195
'''
순열(permutation):
nPr = n!/(n-r)!
조합(combination):
nCr = n!/(n-r)!*r!
'''
# 문제는 끝자리가 0의 갯수 이므로 10의 배수 :2 와 5의 지수의 갯수로 구함

def factorial_5_2_count(num, k):
    count = 0
    while num:
        num//=k
        count+=num
    return count

n, m = map(int, input().split())

five_count = factorial_5_2_count(n,5) - factorial_5_2_count(m,5) - factorial_5_2_count((n-m),5)
two_count = factorial_5_2_count(n,2) - factorial_5_2_count(m,2) - factorial_5_2_count((n-m),2)
# 5와 2 의 지수 중 작은 값
print(min(five_count, two_count))

조합과 순열
https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
# youtube 딩코딩 알고리즘
n=[1,2,3]
r = 2
result = [0]*r
checklist=[0]*len(n)   

def dfs(L):
    if L == r:
        print(result)

    else:
        for i in range(len(n)):
            if checklist[i]==0:
                 result[L] = n[i]
                 checklist[i] =1
                 dfs(L+1)
                 checklist[i] =0

dfs(0)

# youtubve딩코딩 조합
n= [1,2,3]
r= 2
result = [0]*r



def dfs(L, beginwith):
    if L == r:
        print(result)
    else:
        for i in range(beginwith, len(n)):
            result[L] = n[i]
            dfs(L+1, i+1)

dfs(0,0) # 0 level, 0 beginwith


# 30
# 9613 gcd합
# 유클리드 호제법
import sys
input = sys.stdin.readline

def gcd(a,b):
    if a%b!= 0:
        return gcd(b,a%b)
    else:
        return b

t = int(input())

for _ in range(t):
    li = list(map(int, input().rstrip().split()))

    result = 0
    
    for i in range(1, len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                result += gcd(li[i], li[j])
            else:
                result += gcd(li[j], li[i])
    print(result)

# python tool 이용 (itertool, math)
import sys
from itertools import combinations
from math import gcd

input = sys. stdin.readline

t = int(input())

for _ in range(t):
    li = list(map(int, input().rstrip().split()))
    result =0
    coms = combinations(li[1:], 2)
    for a, b in coms:
        result += gcd(a,b)
    print(result)
