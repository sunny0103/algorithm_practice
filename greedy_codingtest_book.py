# 2. 큰수의 법칙
'''  
입력조건: N, M, K 자연수가 주어지며 공백으로 구분
N 개의 자연수가 주어짐 , 입력으로 주어지는 K는 항상 M 보다 작거나 같다. 
출력조건: 큰수의 조건에 따라 더해진 답을 출력
'''
# 1st 
n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
big = data[-1]
second = data[-2]
result = 0

while True:
    for i in range(k):
        if m ==0:
            break
        result += big
        m-=1
    if m ==0:
        break
    result+=second
    m-=1

print(result)

# 수열을 이용한 풀이 
n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
big = data-[1] 
second = data[-2]
count = int(m//(k+1))*k # 가장 큰수를 k번 두번째 큰수를 1번 반복하여 더해지는 횟수
count += m%(k+1) # 더하고 남은 나머지 만큼을 더함
result=0 
result += count*big
result += (m-count)*second
print(result)

# 3. 숫자 카드 게임
'''
입력조건
첫째줄에 숫자 카드들이 놓인 행의 갯수 N과 열의 갯수 M이 공백을 기준으로 각 자연수로 주어짐
둘째줄부터 N개의 줄에 결처 각 카드에 적힌 숫자가 주어짐
출력조건
게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력
'''
# my answer
n, m = map(int, input().split())
mn = []
for i in range(n):
    row = list(map(int, input().split()))
    mn.append(min(row))
print(max(mn))

#1st
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

#2nd
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)

# 4. 1이 될 때까지
'''
입력조건
첫줄에 N과 K가 공백으로 구분되어 각각 자연수로 주어짐. N은 K 보다 항상 크거나 같음
출력조건
N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최소값
'''
# my answer
n, k = map(int,input().split())
count = 0
while True:
    if n ==1:
        break
    elif n%k==0:
        n/=k
        count+=1
    else:
        n-=1
        count+=1
print(count)

# 1st
n ,k = map(int, input().split())
result = 0
while n>=k:
    while n%k !=0:
        n-=1
        result+=1
    n//=k
    result+=1
while n>1:
    n-=1
    result+=1
print(result)

#2nd
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k)*k
    result+=(n-target)
    n = target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)