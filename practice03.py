## DFS example from coding book
# dfs정의
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph =[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 리스트 자료형으로
visited = [False] * 9
dfs(graph, 1, visited)

## bfs예제
from collections import deque

# bfs정의
def bfs(graph, start, visited):
    queue = deque([start])
    #현재노드 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당원소와 연결된 방문하지 않은 원소 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph =[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)

## 음료수 얼려먹기
# 얼음틀 세로 길이 가로길이
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 벗어난 경우 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드 방문하지 않았으면
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상하좌우위치도 재귀적으로 처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)    


## 미로 탈출
#미로 정보 입력
from collections import deque   

n, m = map(int, input().split())
# 그래프 정보 입력
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾을 경우 벗어난 경우
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))

## 럭키 스트레이트
# 점수 입력
n = input()
# 왼쪽 오른쪽 값 리스트 만들기
left = [int(i) for i in n[:len(n)//2]]
right = [int(j) for j in n[len(n)//2:]]
# 조건을 만족하는지 판단
if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')

## 문자열 재정렬
# 문자열 입력
s = input()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
result = ''
for i in s:
    if i in num:
        sum += int(i)
    else:
        result+=i
result=sorted(result)
print(''.join(result)+str(sum))

# from book
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value !=0:
    result.append(str(value))
print(''.join(result))

## 문자열 압축
# from book
def solutions(s):
    # 1개 단위부터 압축단위 늘려가며 확인
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compressed=""
        prev = s[0:step]
        count = 1
        # 단위크기 만큼 증가시키면서 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전과 동일하면 압축 횟수 증가
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count)+ prev if count>=2 else prev
                prev = s[j:j+step] # 상태 초기화
                count=1
         # 남이 있는 문자열에 대홰서 처리
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer, len(compressed))
    return answer

print(solutions('aabbaccc'))

## 자물쇠와 열쇠
# from book

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠 중간 부분 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                # 새로운 자물쇠게 열쇠에 정확히 맞는 지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빽
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))


