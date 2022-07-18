### 다이내믹 
# 51
# 1463 1로 만들기
n = int(input())
dp =[0] *(n+1)
dp[1] = 0
for i in range(2, n+1):
    dp[i] = dp[i-1] +1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1)
    
print(dp[n])

# 52
# 11726 2*n 타일링
n  = int(input())
dp = [0] *(n+1)
dp[1] = 1
if n > 1:
    dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] +dp[i-2]
print(dp[n]%10007)

# 53 
# 11727 2*n  타일링 2
n = int(input())
dp = [0, 1, 3] + [0] * (n-2)

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[n] % 10007)

# 53 
# 2309 일곱 난쟁이
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()
one = 0
two = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarfs) - dwarfs[i]- dwarfs[j] ==  100:
            one = dwarfs[i]
            two = dwarfs[j]
dwarfs.remove(one)
dwarfs.remove(two)
for k in dwarfs:
    print(k)

# 54
# 1748 수 이어쓰기 1
n = int(input())
l = len(str(n))-1
i= 0
result = 0
while i <l:
    result += 9 * (10**i) * (i+1)
    i+=1
result += (l+1)*(n+1-(10**(l)))
print(result)

# 55
# 1476 날짜계산
E, S, M = map(int, input().split())
e, s, m ,year = 0, 0, 0, 0
while True:
    if e == E and s == S and m == M:
        break
    e+=1; s+=1; m+=1; year+=1
    if e ==16:
        e-=15
    if s == 29:
        s -=28
    if m == 20:
        m-=19

print(year)

# 56
# 3085 사탕게임

n = int(input())
li = []

for _ in range(n):
    li.append(list(input()))

def row_count():
    mx = 0
    cnt = 1
    for r in range(n):
        for c in range(n-1):
            if li[r][c] == li[r][c+1]:
                cnt += 1
            else:
                cnt = 1
            mx = max(cnt, mx)
        cnt = 1
    return mx

def col_count():
    mx = 0
    cnt = 1
    for c in range(n):
        for r in range(n-1):
            if li[r][c] == li[r+1][c]:
                cnt += 1
            else:
                cnt = 1
            mx = max(cnt, mx)
        cnt = 1
    return mx

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mx = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if li[i][j] != li[nx][ny]:
                li[nx][ny], li[i][j] = li[i][j], li[nx][ny]
                mx = max(row_count(), col_count(), mx)
                li[i][j], li[nx][ny] = li[nx][ny], li[i][j]

print(mx)

# 57 
# 15649 n과 m 1
n, m = map(int, input().split())
back = []
visited = [False] * (n+1)
def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        back.append(i)
        visited[i] = True
        dfs()
        visited[back.pop()] = False

dfs()

# 58
# 15650 n과 m 2
n, m = map(int, input().split())
back =[]

def dfs(start):
    if len(back) == m:
        print(' '.join(map(str, back)))
        return

    for i in range(start, n+1):
        if i not in back:
            back.append(i)
            dfs(i+1)
            back.pop()

dfs(1)

# 59
# 156751 n과 m 3
n, m = map(int, input().split())
back = []

def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return

    for i in range(1, n+1):
        back.append(i)
        dfs()
        back.pop()

dfs()

# 60
# 15652 n과 m 4
n, m = map(int, input().split())
back = []
def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return
    
    for i in range(1, n+1):
        if not back:
            back.append(i)
            dfs()
            back.pop()
        else:
            if back[-1] <= i:
                back.append(i)
                dfs()
                back.pop()

dfs()

