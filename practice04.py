# ### 코드 업 문제
# ## 스택

# # 01.
# # 1402 : 거꾸로 출력하기 3
# n = int(input())
# li = list(input().split())
# for i in li[::-1]:
#     print(i, end =' ')

# # 02.
# # 1714 : 숫자 거꾸로 출력하기
# num = input()
# for i in num[::-1]:
#     print(i, end='')

# # 03.
# # 2016 : 천단위 구분기호
# n = int(input()) # 숫자 길이
# num = input()
# result = ''
# count = 1
# while count<=n:
#     if count %3 ==0 and n-count != 0:
#         result = ',' + num[n-count]+result
#     else:
#         result = num[n-count]+result
#     count+=1
# print(result)

# # 04.
# # 3117 : 0은 빼!
# n = int(input())
# li = [] 
# for _ in range(n):
#     a = int(input())
#     if a !=0:
#         li.append(a)
#     else:
#         li.pop()

# print(sum(li))


# ### 백준
# ## 200 - 자료구조 1
# # 01.
# # 10828
# import sys

# n = sys.stdin.readline().rstrip()
# li = []

# for i in range(int(n)):
#     a = sys.stdin.readline().split()
#     if a[0] =='push':
#         li.append(int(a[1]))
#     elif a[0] =='pop':
#         print(li.pop() if len(li)>0 else -1)
#     elif a[0] =='size':
#         print(len(li))
#     elif a[0] =='empty':
#         print(1 if len(li)==0 else 0)
#     elif a[0] =='top':
#         print(li[-1] if len(li)>0 else -1)

# 02.
# 단어 뒤집기 9093
