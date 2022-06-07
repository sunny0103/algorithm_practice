# coding test book review

# 큰수의 법칙

# 배열의 크기, 더해지는 횟수, 연속해서 더해질수 있는 횟수입력
n, m, k = map(int, input().split())
# n개의 자연수 입력
li = list(map(int, input().split()))
# 내림차순 정렬
li.sort(reverse=True)
# 높은 수 k 번 두번째 높은 수 1번 을 1차 싸이클로 하여 합을 구함
onetime = li[0]*k + li[1]
# 싸이클이 횟수와 나머지를 더함
result = onetime *(m//(k+1))+ li[0]*(m%(k+1))
print(result)

# 숫자 카드 게임
#  my answer
# 숫자 카드 행렬 입력
n, m = map(int, input().split())
# 숫자 카드 리스트 입력
li = []
for i in range(n):
    li.append(map(int, input().split()))
# 각행의 최솟값을 리스트에 입력 
min_li = []
for j in range(n):
    min_li.append(min(li[j]))
#최솟값 리스트의 최대값
print(max(min_li))

# from book
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)
print(result)

# 1 이 될때까지
# 두 자연수 입력
# my answer
n, k = map(int, input().split())\
# 횟수 초기화
count = 0

while n>1:
    if n%k !=0:
        n-=1
        count+=1
    else: 
        n = n//k
        count+=1

print(count)

# from book
n, k = map(int, input().split())
result = 0

while True:
    # n==k로 나누어지는 수가 될때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k :
        break
    result +=1
    n//= k

result +=(n-1)
print(result)


