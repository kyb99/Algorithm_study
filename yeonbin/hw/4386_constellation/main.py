# 4386 별자리 만들기 231003
# 모든 별들은 서로 이어져 있어야 함.
# 두 별 사이의 거리만큼 비용이 든다.
# 별자리를 만드는 최소 비용 구하기

# 점들 거리 계산하기
# n이 많으면 다 계산하면 시간초과일듯..?
# 가까이 있는거 다 연결? 다익스트라..?

import sys
sys.stdin = open('input.txt')


import heapq
import math

N = int(input())
# 점들 좌표 기억하기
arr = [list(map(float, input().split())) for _ in range(N)]
visited = [0]*N
hq = []
ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        # 간선정보 저장
        dist = math.sqrt((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)
        heapq.heappush(hq, (dist, i, j))

# print(hq)


# 간선정보 제일 작은애부터 빼고 방문표시
# 방문표시 있으면 딴거 ㄱ
dist, a, b = heapq.heappop(hq)
ans += dist

visited[a], visited[b] = 1, 1
# print(visited)

# while hq:
while visited.count(0):
    dist, a, b = heapq.heappop(hq)
    # 갈 곳에 이미 방문했으면 넘어가
    if visited[a] == 1 and visited[b] == 1:
        continue
    # visited[a], visited[b] = 1, 1
    if visited[a] == 0:
        visited[a] = 1
    elif visited[b] == 0:
        visited[b] = 1
    ans += dist
    # print(visited)

print(f'{ans:.2f}')
# print(round(ans, 2))
    


