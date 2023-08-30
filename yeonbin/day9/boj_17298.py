# 오큰수
#  Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1이다
# 총 N개의 수의 오큰수를 공백으로 구분해 출력
'''
4 N(1~1_000_000)
3 5 2 7 Ai(1~1_000_000), i 1~
'''

N = int(input())
arr = list(map(int, input().split()))

# print(arr)

# 3. 결과값을 리스트에 넣도록 하니까 pass
from collections import deque
stack = deque()
s = [0] * N
# 뒤에서부터 스택에 넣자
for i in range(N-1, -1, -1):
    if not stack:
        s[i] = -1
    else:
        if arr[i] < stack[-1]:
            s[i] = stack[-1]
        else:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if not stack:
                s[i] = -1
            else:
                s[i] = stack[-1]
    # push
    stack.append(arr[i])
    print(i, stack)
print(*s)

# 2.
# 더 큰수를 어떻게 찾는게 효율적일까?
# 이진탐색? ㄴㄴ 정렬되어있지않음
# 스택 ㄱ, 결과값을 문자열로 저장해서 프린트
# 이렇게 하면 시간초과
# 2-1
# from collections import deque
# stack = deque()
# s = ''
# # 뒤에서부터 스택에 넣자
# for i in range(N-1, -1, -1):
#     if not stack:
#         s = '-1 ' + s
#     else:
#         if arr[i] < stack[-1]:
#             s = str(stack[-1]) + ' ' + s
#         else:
#             while stack and stack[-1] <= arr[i]:
#                 stack.pop()
#             if not stack:
#                 s = '-1 ' + s
#             else:
#                 s = str(stack[-1]) + ' ' + s
#     # push
#     stack.append(arr[i])
# print(s)
            

# 2-2. 스택 구현 > 시간 초과
# stack = [0]*(N+2)
# top = -1
# s = '' # 뒤에서부터 넣을거니까 답을 여기에 적어줄거임
# # 뒤에서부터 스택에 넣자
# for i in range(N-1, -1, -1):
#     if top == -1: # 빈 스택일때
#         s = '-1 ' + s
#     else: # 빈 스택 아닐때
#         if arr[i] < stack[top]: # 탑값이 더 클때
#             s = str(stack[top]) + ' ' + s
#         else:
#             while top != -1 and stack[top] <= arr[i]:
#                 top -= 1
#             if top == -1:
#                 s = '-1 ' + s
#             else:
#                 s = str(stack[top]) + ' ' + s
#     # push
#     top += 1
#     stack[top] = arr[i]
#     # print(i, top, stack)
# print(s)



# 1.
# 배열을 돌면서, 왼쪽에 나보다 큰수가 있는지 확인하고, 그거 저장
# 맨 마지막은 무조건 -1

# 배열 완전 탐색하는데
# 그거의 오른쪽 애들을 하나씩 탐색
# 시간초과
# for i in range(N-1):
#     for j in range(i, N):
#         # 큰 수 찾으면 프린트 하고 바로 다음 i 검색
#         if arr[i] < arr[j]:
#             print(arr[j], end=' ')
#             break # for j
#     else:
#         print(-1, end=' ')
# print(-1)