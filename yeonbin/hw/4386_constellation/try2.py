# 4386 별자리 만들기 231003 # pass
# 모든 별들은 서로 이어져 있어야 함.
# 두 별 사이의 거리만큼 비용이 든다.
# 별자리를 만드는 최소 비용 구하기

# 점들 거리 계산하기
# n이 많으면 다 계산하면 시간초과일듯..?
# 가까이 있는거 다 연결? 다익스트라..?

# import sys
#
# sys.stdin = open('input.txt')

import heapq
import math

N = int(input())
# 점들 좌표 기억하기
arr = [list(map(float, input().split())) for _ in range(N)]
visited = [0] * N
hq = []
ans = 0

# 간선정보 제일 작은애부터 빼고 방문표시
# 방문표시 있으면 딴거 ㄱ

visited[0] = 1
for i in range(1, N):
    dist = math.sqrt((arr[i][0]-arr[0][0])**2+(arr[i][1]-arr[0][1])**2)
    heapq.heappush(hq, (dist, 0, i))

while visited.count(0):
    dist, now, nxt = heapq.heappop(hq)
    if visited[nxt] == 1:
        continue
    ans += dist
    visited[nxt] = 1
    # 여기서 가능한 별자리 다 넣기
    for i in range(N):
        if i == nxt:
            continue
        dist = math.sqrt((arr[i][0] - arr[nxt][0]) ** 2 + (arr[i][1] - arr[nxt][1]) ** 2)
        heapq.heappush(hq, (dist, nxt, i))


print(f'{ans:.2f}')
# print(round(ans, 2))



