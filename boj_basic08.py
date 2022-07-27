# 80
# 11047 동전 0
n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

cnt = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if coins[i] > k:
        continue
    cnt += k // coins[i]
    k = k % coins[i]
print(cnt)
'''
나의 풀이 왜 틀린지 모르겠다......
# coins.sort(reverse=True)
# cnt = 0
# i = 0
# while k >0:
#     if k > coins[i]:
#         cnt += k // coins[i]
#         k = k % coins[i]
#     else:
#         i+=1
# print(cnt)

'''

# 81
# 11399 atm
n = int(input())
li = list(map(int, input().split()))
li.sort()
total = 0
times = []
for i in li:
    total += i
    times.append(total)
print(sum(times))

# 82
# 10610 30
'''
각 자리수의 합이 3의 배수이면서 1의 자리수가 0 이어야 30 의 배수
'''
n = list(input())
n.sort(reverse= True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 !=0 or'0' not in n:
    print(-1)
else:
    print(''.join(n))

# 83
# 1783 병든 나이트
n, m = map(int, input().split())

if n ==1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m-2)

84
10815 숫자 카드
'''
하나씩 찾는 것을 요구하는 문제는 아닐 것이므로 해답이 될수 없음

n = int(input())
nli = list(map(int, input().split()))
m = int(input())
mli = list(map(int, input().split()))
nli.sort()
result  = [0] * len(mli)
for idx, i in enumerate(mli):
    for j in nli:
        if i  == j:
            result[idx] = 1

print(' '.join(map(str,result)))
'''

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
card.sort()

def binary(array, target,start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary(card, check[i], 0, n-1) is not None:
        print(1, end =' ')
    else:
        print(0, end =' ')

# 85
# 10816 숫자 카드 2

n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

hash = {}
for i in card:
    if i in hash:
        hash[i]+=1
    else:
        hash[i] = 1
'''

# for j in check:
#     if j in hash:  
#         print(hash[j], end=' ')
#     else:
#         print(0, end=' ')
'''
for j in check:
    result = hash.get(j)
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')

# 86
# 11728 배열 합치기
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = a +b 
result.sort()
print(*result)  # print(' '.join(map(str, result)))

# 87
# 10989 수 정렬하기 3
import sys
input = sys.stdin.readline
n = int(input())
li = [0]*10001
for _ in range(n):
    li[int(input())]+=1

for i in range(10001):
    if li[i]!=0:
        for j in range(li[i]):
            print(i)

# 88
# 10825 국영수
'''
람다 - 를 이용하여 reverse 를 할수 있다. 
'''
n = int(input())
array = []
for _ in range(n):
    n, k, e, m = list(input().split())
    array.append([n, int(k), int(e), int(m)])

array.sort(key= lambda x: (-x[1], x[2], -x[3], x[0])) 

for i in array:
    print(i[0])

# 89
# 11652 카드
n = int(input())
dic = {}
for _ in range(n):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
sdic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(sdic[0][0])

# 90
# 2751 수 정렬하기 2
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

li.sort()
for i in li:
    print(i)