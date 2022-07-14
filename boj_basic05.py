### 다이나믹 프로그래밍
# 41
# 1912 연속 합
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split()))
tot = [li[0]]
for i in range(1, n):
    tot.append(max(li[i], tot[i-1]+li[i]))

print(max(tot))

# 42 
# 2225 합분해
n, k = map(int, input().split())

dp =[[0]*(n+1) for _ in range(k+1)]

for i in range(k+1):
    for j in range(n+1):
        if i ==1:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1] +dp[i-1][j])% 1000000000

print(dp[k][n])

# 43
# 1699 제곱수
# https://pacific-ocean.tistory.com/205
n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = i
    for j in range(1,i):
        if j**2 > i:
            break
        if dp[i]> dp[i - j**2]+1:
            dp[i] = dp[i -j**2]+1
print(dp[n])
'''
# 틀린다고 나온 내가 만든 코드... 이유는 아직 모르겠음....
m = int(input())
dp1 = [0]*(n+1)

for i in range(1,m+1):
    dp1[i] = dp1[i-(int(i**0.5)**2)] + 1
print(dp1[n])
'''

# 44
# 2193 이친수
n = int(input())
nn = [0]*(n+1)
nn[1] = 1
for i in range(2, n+1):
    nn[i] = nn[i-1] +nn[i-2]
print(nn[n])

# 45
# 9095 1,2,3더하기
t = int(input())
array = [1, 2, 4]
for i in range(3, 10):
    array.append(array[i-1]+array[i-2]+array[i-3])

for _ in range(t):
    print(array[int(input())-1])

# 46
# 1932 정수 삼각형
n  = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

for r in range(1, n):
    for c in range(len(mat[r])):
        if c == 0:
            mat[r][c] = mat[r-1][c] + mat[r][c]
        elif c == len(mat[r])-1:
            mat[r][c] = mat[r-1][c-1] + mat[r][c]
        else:
            mat[r][c] = max(mat[r-1][c-1],mat[r-1][c]) + mat[r][c]
print(max(mat[-1]))

# 47 
# 1149 RGB 거리
'''
나의 풀이 : 각 열의 최소 값을 찾고  rbg고려 하는 형태 였으나 
각 rgb의 최소를 구하는 형태로 구현하여야 함

n = int(input())
rgb = [True]*n 
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
total = 0
idx = 0
for r in range(n):
    mn = max(cost[r])
    for c in range(3):
        if rgb[c] == True and mn >= cost[r][c]:
            mn = cost[r][c]
            idx = c
    print(mn)
    total += mn
    rgb = [True] * n 
    rgb[idx] = False
print(total)
'''
n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]
print(min(cost[n-1]))

# 48
# 2156 포도주 시식
# https://pacific-ocean.tistory.com/152
n = int(input())
w = [0]
for _ in range(1, n+1):
    w.append(int(input()))
dp = [0]
dp[1] = w[1]
if n >1:
    dp.append(w[1]+w[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1],dp[i-2]+w[i],dp[i-3]+w[i]+w[i-1]))
print(dp[n])

# 49
# 10844 쉬운 계단수
n = int(input())
array =[[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    array[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            array[i][j] = array[i-1][1]
        elif j == 9:
            array[i][j] = array[i-1][8]
        else:
            array[i][j] = array[i-1][j-1] + array[i-1][j+1]
print(sum(array[-1])%1000000000)

# 50
# 11052 카드 구매하기
n = int(input())
cards = [0] + list(map(int, input().split()))
result = [0] *(n+1)
result[1] = cards[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if result[i] < result[i-j] + cards[j]:
            result[i] = result[i-j] + cards[j]
print(result[n])