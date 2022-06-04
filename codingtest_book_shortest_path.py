# 간단한 데이크스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미

n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)
#간선정보 입력하기
for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중 가장 짧은 최단거리 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작노드를 제외한 전체 n-1노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] +j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
#알고리즘 수행
dijkstra(start)

#모든 노드 최단거리 출력
for i in range(1, n+1):
    if distance[i]==INF:
        print('Infinity')
    else:
        print(distance[i])


# 개선된 데이크스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #누함을 의미하는 10억\

#입력받기
# 노드 갯수, 간선
n, m = map(int, input().split())
# 시작노드
start = int(input())
#각 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
#최단거리 데이블을 무한으로 초기화
distance = [INF] * (n+1)

# 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstras(start):
    q = []
    # 시작노드로 가기 위한 최단 경로 0 으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # q가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
             cost = dist + i[1]
             #현재 노드를 거쳐 다른 노드가 더 짧은 경우
             if cost < distance[i[0]]:
                 distance[i[0]] = cost
                 heapq.heappush(q, (cost, i[0]))

dijkstras(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('Infinity')
    else:
        print(distance[i])

# 플로이드 워셜 알고리즘
INF = int(1e9)

#노드 갯수와 간선 갯수 입력
n = int(input())
m = int(input())
# 2차원 리스트 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
#자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0 

# 간선 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]  = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('Infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# 실전 문제 
# 미래도시
# 노드 갯수와 간선갯수 입력
n, m = map(int, input().split())
# 무한을 의미한는 값 설정
INF = int(1e9)
# 2차원 리스트를 만들고 무한으로 초기화
graph = [[INF] *(n+1) for _ in range(n+1)]
# 자기자신으로 가는 비용은 0 으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 간선에 대한 정보를 입력받아 값 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# 거처갈 노드와 목적지 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
distance = graph[1][k] +graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 도시 갯수, 통로갯수, 메세지를 보내고자 하는 도시
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단거리를 담는 리스트
distance = [INF] * (n+1)

# 간선정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    # x에서 y 로 가는 노드의 비용이 z
    graph[x].append((y, z))

def dikstras(start):
    q = []
    # 시작노드로 가기위한 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        #인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dikstras(start)

# 도달할 수 있는 노드의 갯수
count = 0
# 도달할 수 있는 노드 중 가장 먼 노드의 최단거리
max_distance = 0
for d in distance:
    if d != INF:
        count+=1
        max_distance = max(max_distance, d)

# 시작노드 제외 count-1
print(count-1, max_distance)