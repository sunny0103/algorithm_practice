#### coding test book review
### 구현
## 상하좌우 문제
# 공간의 크기 입력
n = int(input())
# 여행 계획서 내용
p = list(input().split())
x, y = 1, 1
# 상하좌우 리스트
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
pxy = ['L', 'R', 'U', 'D']

for i in p:
    for j in range(len(pxy)):
        if i == pxy[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx <1 or nx>n or ny<1 or ny>n:
        continue
    x, y = nx, ny
print(x, y)

## 시각
# 시각 정수 입력
n = int(input())
# 3 이 하나라도 포함되는 경우의 수
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if  '3' in str(i) + str(j) + str(k):
                count+=1
print(count)

## 왕실 나이트
loca = input()
row = int(loca[1])
col = (ord(loca[0]))- (ord('a')) +1
# 나이트가 갈수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),(-2, 1)]
count = 0
for step in steps:
    nx = row +step[0]
    ny = col +step[1]
    if nx<1 or nx>8 or ny <1 or ny >8:
        continue
    count+=1
print(count)

## 게임개발
# 맵의 크기 입력
n, m = map(int, input().split())
# 좌표와 방향 입력
x, y, direction = map(int, input().split())
# 방문위치  초기화
d = [[0]*m for _ in range(n)]
# 현재 방문 좌표 방문처리
d[x][y] = 1
# 맵정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
  
# 북동남서 방향 처리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction == -1:
        direction =3
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면에 가지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count+=1
        turn_time = 0
        continue
    else:
        turn_time+=1
    # 네방향 모두 갈수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)

### 그리디
## 모험가 길드
# 모험가 수 입력
n = int(input())
# 모험가의 공포도 입력, 정렬
d = list(map(int, input().split()))
d.sort()
# 그룹수 초기화
result = 0
# 현그룹의 모혐가의 수
count = 0
for i in d:
    count+=1
    if count >=i:
        result+=1
        count =0
print(result)

## 곱하기 혹은 더하기
#  숫자로만 이루어진 문자열 입력
s = input()
# 각 문자열을 숫자로 변환
s = [ int(s[i]) for i in range(len(s))]
# 결과 초기화
result = 0
# 곱 또는 더하기 
for i in s[1:]:
    if i <= 1 or result <= 1:
        result+=i
    else:
        result*=i
print(result)

## 문자열 뒤집기
s = input()
count0 = 0  # 전부 0 으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소
if s[0] =='1':
    count0 += 1
else:
    count1 += 1

#두번재 원소부터 
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0,count1))
        
## 만들수 없는 금액
# 동전의 갯수 입력
n = int(input())
# 화폐단위 입력, 오름차순 정렬
c = list(map(int, input().split()))
c.sort()
# 가능한 동전 금액 
total = []

for i in range(n):
    for j in range(1, n+1):
        if i<=j:
            total.append(sum(c[i:j]))

# 만들수 있는 동전중 최소값 출력
total = list(set(total))
for i in range(max(total)+1):
    if i not in total:
        print(i)
        break

## from book
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target+=x
print(target)

## 볼링공 고르기
## from book
# 볼링공 갯수 공의 무게 입력
n, m = map(int, input().split())
# 볼링공 무게 입력
data = list(map(int, input().split()))
# 1-10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x]+=1

result = 0
for i in range(1, m+1):
    n-=array[i]
    result += array[i]*n
print(result)

##  무지의 먹방 라이브
## my answer
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    while sum(food_times) >0 and k>=0:
        for idx in range(len(food_times)):
            if food_times[idx] !=0 and k!=0:
                food_times[idx]-=1
                k-=1
            elif food_times[idx] !=0 and k ==0:
                return idx+1
            elif food_times[idx] ==0 and k!=0:
                continue
            else:
                return idx+1

print(solution([3,1,2], 5))

## from book
import heapq
def solution(food_times, k):
    # 음식 전체를 먹는 시간보다 k가 더 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value + ((q[0][0]) - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 음식 번호를 기준으로 정렬
    result = sorted(q, key= lambda x: x[1])
    return result[(k-sum_value)%length][1]

print(solution([3,1,2], 5))