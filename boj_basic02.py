# ### 백준
# ## 자료구조 (연습)
# # 11.
# # 17298 오큰수
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().rstrip().split()))
# stack =[]
# answer = [-1]*n

# for i in range(len(arr)):
#     while stack and arr[stack[-1]] < arr[i]:
#         answer[stack.pop()]= arr[i]
#     stack.append(i)

# print(*answer)

# # 12.
# # 17299 오등큰수

# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().rstrip().split()))
# answer = [-1]*n
# stack =[]
# for i in range(len(arr)):
#     while stack and arr.count(arr[stack[-1]]) < arr.count(arr[i]):
#         answer[stack.pop()]= arr[i]
#     stack.append(i)

# print(*answer)

# # 13.
# # 1918 후위표기식
# https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python
# import sys

# strings = sys.stdin.readline().rstrip()
# stack = []
# result =""

# for s in strings:
#     if s.isalpha():
#         result+=s
#     else:
#         if s == "(":
#             stack.append(s)
#         elif s in ['*','/']:
#             while stack and stack[-1] in ['*','/ ']:
#                 result+=stack.pop()
#             stack.append(s)
#         elif s in ['+', '-']:
#             while stack and stack[-1] !="(":
#                 result+=stack.pop()
#             stack.append(s)
#         elif s ==")":
#             while stack and stack[-1]!="(":
#                 result+=stack.pop()
# while stack:
#     result+=stack.pop()
# print(result)

# 14.                                                                                                                   
# 1935 후위표기식 2
# import sys

# input = sys.stdin.readline
# n = int(input())
# strings = input().rstrip()
# num = [0]*n
# for i in range(n):
#     num[i]= int(input().rstrip())

# stack =[]

# for s in strings:
#     if s.isalpha():
#         stack.append(num[ord(s)-ord('A')])
#     else:
#         str2 = stack.pop()
#         str1 = stack.pop()

#         if s == '+':
#             stack.append(str1+str2)
#         elif s=='-':
#             stack.append(str1-str2)
#         elif s=='*':
#             stack.append(str1*str2)
#         elif s =='/':
#             stack.append(str1/str2)

# print('%.2f'%stack[0])

# # 15.
# # 10808 알파벳 갯수
# import sys
# input = sys.stdin.readline

# num_list = [0]*26 # 알파벳 갯수
# strings = input().rstrip()

# for s in strings:
#     num_list[ord(s)-ord('a')]+=1

# for num in num_list:
#     print(num, end=' ')

# # 16.
# # 10809 알파벳 찾기
# import sys

# input = sys.stdin.readline
# num_list = [-1]*26
# strings = input().rstrip()

# for i in range(len(strings)):
#     if num_list[ord(strings[i])-ord('a')] == -1:
#         num_list[ord(strings[i])-ord('a')] = i
#     else:
#         continue

# for num in num_list:
#     print(num, end=' ')

# 17.
# 10820 문자열 분석



