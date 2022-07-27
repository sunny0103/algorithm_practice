# 61
# 15654 n과 m 5
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
back = []
def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return

    for i in li:
        if i not in back: 
            back.append(i)
            dfs()
            back.pop()

dfs()

# 62
# 15655 n과 m 6
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
back = []
def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
    
    for i in li:
        if i not in back:
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

# 63
# 15656 n과 m 7
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
back = []

def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return 

    for i in li:
        back.append(i)
        dfs()
        back.pop()

dfs()

# 64
# 15657 n과 m 8
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
back = []

def dfs():
    if len(back) == m:
        print(' '.join(map(str, back)))
        return

    for i in li:
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

# 65
# 10972 다음순열 
'''
next permutation
ex 1432
규칙
1. 순열을 뒤에서 부터 비교하여 뒤값이 앞에 값보다 큰경우를 찾는다
(3,2), (4,3) 은 해당되지 않고,  (1,4) 가 이에 해당
x- 1, y-4
2. 뒤에서 부터 값을 비교하여 x 보다 큰 값과 스왑
즉,1 과 2의 자리를 변경해 준다
2 4 3 1 이 됨
3. 여기서 y값인 4부터 오름차순으로 정리
2 1 3 4
'''
n = int(input())
li = list(map(int, input().split()))
x = 0
for i in range(n-1, 0, -1):
    if li[i] > li[i-1]:
        x = i-1
        break

for j in range(n-1, 0, -1):
    if li[x] < li[j]:
        li[j], li[x] = li[x], li[j]
        li = li[:x+1] + sorted(li[x+1:])
        print(*li) # *을 이용해 공백을 사용하여 모든 리스트의 값을 출력
        exit()
print(-1)
    
# 66
# 10973 이전순열
'''
다음 순열과 정 반대로 구현 하면 됨
'''
n = int(input())
li = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if li[i] < li[i-1]:
        x = i-1
        for j in range(n-1, 0, -1):
            if li[x] > li[j]:
                li[x], li[j] = li[j], li[x]
                li = li[:x+1] + sorted(li[x+1:], reverse=True)
                print(*li)
                exit()
print(-1)

# # 67
# # 10974 모든순열
n = int(input())
back =[]
def permu():
    if len(back) == n:
        print(' '.join(map(str, back)))
        return
    
    for i in range(1, n+1):
        if i not in back:
            back.append(i)
            permu()
            back.pop()

permu()

# 68
# 14501 퇴사
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
total = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + li[i][0] > n:
        total[i] = total[i+1]
        print(total[i])
    else:
        total[i] = max(li[i][1] + total[i + li[i][0]], total[i+1])
        print(total[i])

        
print(total)

# 69
# 11723 집합
import sys
input = sys.stdin.readline
n = int(input())
s = set()
for i in range(n):
    command = input().rstrip().split()
    if len(command) == 1:
        if command[0] == 'all':
            s = set(i for i in range(1, 21))
        else:
            s = set()

    elif len(command) == 2:
        com, num = command[0], int(command[1])
        if com == 'add':
            s.add(num)
        elif com == 'remove':
            s.discard(num)
        elif com == 'check':
            print(1 if num in s else 0)
        elif com =='toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)

# 70
# 2875 대회 or 인턴
n, m, k = map(int, input().split())
cnt = 0 
while n + m >= k and n >= 0 and m >= 0:
    n -= 2
    m -= 1
    cnt += 1

print(cnt-1)
