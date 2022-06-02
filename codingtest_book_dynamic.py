# 피보나치 수열 재귀 탑다운
d = [0]*100

def fibo(x):
    print('f('+str(x)+')',end=' ')
    if x == 1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+ fibo(x-2)
    return d[x]

print(fibo(6))

# 피보나치 수열 반복 버텀업
d = [0]*100
d[1] = 1
d[2] = 1
n=10

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

# 1로 만들기
x = int(input())
d = [0]*30001

for i in range(2, x+1):
    d[i] = d[i-1]+1
    if i%2 ==0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 ==0:
        d[i]= min(d[i], d[i//3]+1)
    if i%5 ==0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

# 개미전사
n = int(input())
array = list(map(int, input().split()))
d =[0]*100

d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])
print(d[n-1])

# 바닥공사
n = int(input())
d= [0]*1001
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+d[i-2]*2)%796796
print(d[n])

# 효율적 화폐구성
n, m = map(int, input().split())
array =[]
for i in range(n):
    array.append(int(input()))

d = [10001] *(m+1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] !=10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])