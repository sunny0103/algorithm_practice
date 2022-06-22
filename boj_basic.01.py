### 백준
## 200 - 자료구조 1
# 01.
# 10828 스택
import sys

n = sys.stdin.readline().rstrip()
li = []

for i in range(int(n)):
    a = sys.stdin.readline().split()
    if a[0] =='push':
        li.append(int(a[1]))
    elif a[0] =='pop':
        print(li.pop() if len(li)>0 else -1)
    elif a[0] =='size':
        print(len(li))
    elif a[0] =='empty':
        print(1 if len(li)==0 else 0)
    elif a[0] =='top':
        print(li[-1] if len(li)>0 else -1)

# 02.
# 9093 단어 뒤집기 
t = int(input())
lists = []
for _ in range(t):
    lists.append(list(input().split()))

for li in lists:
    for j in li:
        print (j[::-1], end=' ') 
    print()

# 03. 
# 9012 괄호
'''
"(" 을 1 ")"을 -1 로 하여 총 합이 0 일 경우 yes를 0이외의 값은  no를 반환하는 프로그램을 작성
'''
n = int(input())

def vps(strings):
    result = 0
    for i in range(len(strings)):
        if strings[i] =="(":
            result+=1
        elif strings[i] ==")":
            result-=1

    if result == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(n):
    print(vps(input()))

# 04. 
# 1874 스택수열
n = int(input())
stack = []
answer = []
count = 1 
flag = 0
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count+=1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = 1
        break
if flag ==1:
    print('NO')
else:
    for i in answer:
        print(i)

# 05.
# 1406. 에디터
# https://seongonion.tistory.com/53
import sys
st1 = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
st2 =[]

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] =='D':
        if st2:
            st1.append(st2.pop())
    elif command[0] =='B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))

# 06. 
# 10845 큐
import sys
from collections import deque
queue = deque()

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] =='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif command[0] =='front':
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] =='back':
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[-1])  

# 07. 
# 1158. 요세프스
# https://infinitt.tistory.com/213
n, k = map(int, input().split())
li = [i for i in range(1, n+1)]
result = []
num = 0

for i in range(n):
    num+=k-1
    if num>= len(li):
        num = num%len(li)
    result.append(str(li.pop(num)))

print("<",', '.join(result[:]),">",sep='')


# 08. 
# 10866 덱
import sys
from collections import deque
queue = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
        if len(queue) == 0:
           print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

# 09.
# 17413 단어 뒤집기
import sys

strings = sys.stdin.readline().rstrip()
tag = False
q = ""
s = ""
for i in range(len(strings)):
    if tag == False:
        if strings[i] == "<":
            tag = True
            q+=strings[i]
            if s !="":
                print(s[::-1], end='')
                s = ""
        else:
            if strings[i] !=" ":
                s+=strings[i]
                if i==len(strings)-1:
                    print(s[::-1], end='')
            else:
                print(s[::-1], end=' ')
                s = ""
    else:
        q+=strings[i]
        if strings[i]==">":
            print(q,end='')
            tag = False
            q = ""

# 10.
# 10799 쇠막대기
import sys

arr = sys.stdin.readline().rstrip()
stack= []
answer = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(0)
    else:
        if arr[i-1] =="(":
            stack.pop()
            answer+=len(stack)   
        else:
            stack.pop()
            answer+=1 

print(answer)