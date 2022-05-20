# 알고리즘 기초문제외 기출연습 2 개만
# 상하좌우
'''
입력조건
첫줄에 공간의 크기를 나타내는 N
둘째줄에 여행가 A 의 이동계획서
출력조건
여행가 A의 최종 좌표출력
'''
n = int(input())
x ,y = 1, 1
plans = input().split()

# L,R,U,D
dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]
move_types =['L','R','U','D']

# 이동계획 실행
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <1 or ny <1 or nx>n or ny>n:
        continue
    x, y = nx, ny

print(x, y)

# 시각
'''
입력조건
정수 N입력
출력조건
00시00분00초부터 N시 59분 59초까지 모든 시각중 3이 하나라도 포함된 경우
'''
n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) +str(k):
                count +=1

print(count)


# 왕실 나이트
'''
입력조건
첫째 줄에 8X8좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 문자로 구성된 열이 입력
출력조건
나이트가 이동할 수 있는 경우의 수를 출력
'''
# from book 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1
# 나이트가 이동할 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동가능 하다면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
        result+=1

print(result)

# 게임개발.  
'''
입력조건 
첫째줄 세로크기N, 가로크기M을 공백을 구분하여 입력
둘째줄 캐릭터의 좌표와 방향이 공백을 구분하여 입력
섯째줄 맵이 바다인지 육지인지 구분되어 정렬
출력 
캐릭터가 방문한 칸의 수 출력 
'''

# from book
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵성하여 0 으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 캐릭터 좌표, 방향 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time =0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않는 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count+=1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0                                       
print(count)

# 7. 럭키 스트레이트
'''
입력조건
점수 N이 정수로 주어지며 짝수형태
출력 조건
럭키 스트레이트를 사용 할 수 있다면 LUCKY 사용할수 없다면 READY를 출력
'''
n = input()

left = [int(i) for i in n[:(len(n)//2)]]
right = [int(i) for i in n[(len(n)//2):]]
if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')

# from book
n = input()
length = len(n)
summary = 0
# 왼쪽 부분 자릿수 합
for i in range(length//2):
    summary+=int(n[i])
#오른쪽 부분
for i in range(length//2, length):
    summary-=int(n[i])
# 왼쪽과 오른쪽이 동일한 지 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')

# 문자열 재정렬
'''
입력조건
첫째줄에 문자열 S가 주어짐
출력조건 알파벳은 오름차순, 모든 숫자는 더하여 이어서 출력
'''
# my answer
s = input()
letter = []
num = 0
for i in s:
    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num += int(i)
    else:
        letter.append(i)
        letter.sort()

letter =''.join(letter)
result = letter+str(num)
print(result)

# from book
data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)
# 알파벳을 오름차순으로 정렬
result.sort()
# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!=0:
    result.append(str(value))
print(''.join(result))



