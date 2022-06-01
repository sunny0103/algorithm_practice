# 부품 찾기
# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0 , n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수정렬
n = int(input())
array = [0]* 1000001

for i in input().split():
    array[int(i)] =1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 집합 자료형
n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 떡볶이 떡 만들기
n, m = list(map(int, input().split()))
li = list(map(int, input().split()))

start = 0
end = max(li)

result = 0
while start <= end:
    tot = 0
    mid = (start + end)//2
    for i in li:
        if i > mid:
            tot += i- mid
    if tot <m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)