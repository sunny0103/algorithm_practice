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

# 01. 모험가 길드
'''
입력조건
첫줄에 모험가의 수
둘째 줄에 모험가의 공포도 값을 N이하의 자연수로 공백으로 구분
출력 조건
여행을 떠날 수 있는 그룹수를 최댓값으로 출력
'''
n = int(input())
data = sorted(list(map(int, input().split())))
result = 0
count = 0
for i in data:
    count+=1
    if count>=i:
        result+=1
        count = 0
print(result)

# 02. 곱하기 혹은 더하기
'''
입력조건
첫째 줄에 여라 갯의 숫자로 구성된 하나의 문자열 S가 주어짐
출력조건
첫째 줄에 만들어질 수 있는 가장 큰 수를 출력
'''
# my answer
s = input()
li= list(map(int, list(s)))
result = 1
for i in li:
    if i !=0 and i!=1:
        result*=i
    else:
        result+=i
print(result)

# from book
data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <=1:
        result+=num
    else:
        result*=num
print(result) 

# 문장열 뒤집기
'''
입력조건
첫째 줄에 0 과 1로만 이루어진 문자열 S가 주어짐
출력조건
행동의 최소 횟수 출력
'''
# my answer
s = input()
s = list(map(int,list(s)))
diff = []
result = 1
for i in range(1, len(s)):
    if s[0] != s[i]:
       diff.append(i)
if len(diff) < len(s)-len(diff):
    for j in range(1,len(diff)):
        if diff[j-1]!=diff[j]-1:
            result+=1
else:
   for j in [i for i in range(len(s))]-diff:
       if s[j]!=s[j+1]+1:
           result+=1
print(result)

# book
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0+=1
        else:
            count1+=1

print(min(count0, count1))

# 만들 수 없는 금액
'''
입력조건
첫째 줄 동전 갯수를 나타내는 양의 정수 N
둘째 줄 각 동전의 단위를 나타내는 N개의 자연수, 공백으로 구분
출력조건
각 동전들로 만들수 없는 양의 정수의 금액중 최솟값
'''
# my answer
n = int(input())
coins = sorted(list(map(int, input().split())))
li =[]

while n!=0:
    for i in range(n):
        li.append(sum(coins[i:n]))
    n-=1

li = sorted(set(li))
for i in range(min(coins),max(li)):
    if i not in li:
        print(i)
        break

# book
n = int(input())
data= list(map(int, input().split()))
data.sort()
target = 1
for x in data:
    if target < x:
        break
    target+=x
print(target)

# 5. 볼링공 고르기
'''
입력조건
첫째 줄 볼링공의 갯수 N 공의 최대무게 M 이 공백으로 구분되어 자연수
둘째 줄 볼링공의 무게 K 가 공백으로 구분되어 자연수의 형태로 주어짐
출력조건
볼링공을 고르는 두사람의 경우의 수 출력
'''
# my answer
n, m = map(int, input().split())
k = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(1+i, n):
        if k[i] != k[j]:
            count+=1
print(count)

# book
n, m = map(int, input().split())
data = list(map(int, input().split()))
# 1- 10 까지 무게를 담는 리스트
array =[0]*11
# 각 무게에 해당하는 볼링공의 갯수 카운트
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n-=array[i] # 무게가 i인 볼링공의 갯수 제외(A가 선택할수 있는 갯수)
    result+=array[i]*n # B가 선택하는 경우의 수와 곱

# 6. 무지의 먹방 라이브
'''
제한사항
food_times 는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열
k는 방송이 중단된 시간
더 섭취 해야할 임식이 없다면 -1을 반환
'''
# from book
import heapq

def solution(food_times,k):
    if sum(food_times) <=k:
        return -1

    q=[]
    for i in range(len(food_times)):
        # 음식 시간, 음식 번호 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i],i+1))

    sum_value = 0 # 먹기위해 사용한 시간
    previous =0 # 지전에 다 먹은 음식시간
    length = len(food_times)

    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous)*length
        length -=1
        previous = now
    
    result = sorted(q, key = lambda x : x[1]) #음식번호 기준으로 정렬
    return result[(k-sum_value)%length][1]

