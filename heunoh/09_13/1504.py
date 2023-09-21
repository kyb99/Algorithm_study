# 응 틀렸어
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)
res = []
N, E = map(int, input().split())
arr = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, N+1):
        if i == j:
            arr[i][j] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c

v1, v2 = map(int, input().split())

# k = 거쳐가는 노드란다
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in arr:
    print(i)
route1 = arr[1][v1] + arr[v1][v2] + arr[v2][N]
route2 = arr[1][v2] + arr[v2][v1] + arr[v1][N]
# ㅅㅂtqtqtqtqㅠㅠ
print(route1, route2)
print(min(route1, route2))