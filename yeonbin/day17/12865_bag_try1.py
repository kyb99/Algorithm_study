# 평범한 배낭 # 230929
# N개의 물건, 무게 W, 가치 V
# 배낭 K, 가치의 최댓값?

# N이 100이니까 백트래킹은 안될듯..?
# 일단 가치가 큰것부터?
# 가치가 0이면 패스, 무게가 K보다 크면 패스
# 그래도 일단 백트래킹 해봐?
# 역시 시간초과
def backtrack(lv, acc, val):
    global max_v
    # print(lv, acc, val, visited)
    # 기저조건
    if acc > K:
        return
    if max_v < val:
        max_v = val
    if lv == N:
        return
    # 함수드가자
    for i in range(lv+1, N):
        if not visited[i]:
            visited[i] = 1
            backtrack(lv+1, acc+arr[i][0], val+arr[i][1])
            visited[i] = 0


N, K = map(int, input().split())
# W V
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
max_v = 0

backtrack(0, 0, 0)

print(max_v)
# print(arr)