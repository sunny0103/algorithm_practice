# 음료수 얼려먹기
'''
입력조건
첫줄에 얼음 틀의 세로 N과 가로M 이 주어짐
두번째 줄 N+1번 째 줄까지 얼음 틀의 형태가 주어짐
구멍이 뚫린 부분은  0 그렇지 않은 부분은 1
출력조건
한번에 만들수 있는 아이스 크림의 갯수
'''
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <=-1 or y >=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1
print(result)

# 미로탈출
from collections import deque
import queue

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 정의 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우
            if nx <0 or nx>=n or ny<0 or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[n-1][m-1]
print(bfs(0,0))