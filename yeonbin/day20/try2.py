# 유니온파인드처럼..?
# 처음 붙일때 부모를 저장해서 붙이자
# 틀림... 왜?
'''
반례: 나중에 연결시키는 경우
6
1 2
2 3
4 5
4 6
1 4
2
2 5
5 6
'''

import sys
sys.stdin = open('input.txt')

# 이거 안썼음
# def find(x):
#     if parent[x] == x:
#         return x
#     else:
#         return find(parent[x])


N = int(input())
# tree = [[] for _ in range(N+1)]
parent = [[i] for i in range(N+1)]
# print(parent)

# # 트리 입력받기
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     if a == 1:
#         parent[b] = parent[1] + parent[b]
#     elif b == 1:
#         parent[a] = parent[1] + parent[b]
#     elif parent[a] == [a]:
#         parent[a] = parent[b] + parent[a]
#     else:
#         parent[b] = parent[a] + parent[b]
# # print(parent)

# # 알고싶은 쌍
# M = int(input())
# for _ in range(M):
#     a, b = map(int, input().split())
#     for i in range(len(parent[a])-1, -1, -1):
#         if parent[a][i] in parent[b]:
#             print(parent[a][i])
#             break # for i


for _ in range(N-1):
    a, b = map(int, input().split())
    if a == 1:
        parent[b] = parent[b] + parent[1]
    elif b == 1:
        parent[a] = parent[b] + parent[1]
    elif parent[a] == [a]:
        parent[a] = parent[a] + parent[b]
    else:
        parent[b] = parent[b] + parent[a]
print(parent)

# 알고싶은 쌍
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    for p in parent[a]:
        if p in parent[b]:
            print(p)
            break # for i

# 현기오빠는 레벨을 저장+바로 위의 부모 저장해서
# 레벨 맞춘후에 부모찾는 방식으로 풀었다.