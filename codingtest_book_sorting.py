#  위에서 아래로
# my answer
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)
for i in li:
    print(i, end=' ')

# 성적이 낮은 순서로 학생 출력하기
n = int(input())
li = []
for i in range(n):
    data = input().split()
    li.append((data[0], int(data[1])))

li = sorted(li, key = lambda v: v[1])

for j in li:
    print(j[0], end=' ')

# 두 배열의 원소 교체
# my answer with book 
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
