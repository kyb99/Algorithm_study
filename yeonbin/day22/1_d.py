# 231025
# try2

import sys
sys.stdin = open('input.txt')

# 포인트는 축을 비용으로 잡는것!
# 1차원으로 다시 도전했다!
N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

max_cost = sum(costs)

dp = [0]*(max_cost+1)

result = max_cost + 1

for i in range(N):
    for j in range(max_cost, -1, -1):
        # 범위를 벗어나는 경우
        if costs[i] + j > max_cost:
            continue
        else:
            dp[costs[i] + j] = max(dp[costs[i] + j], dp[j] + memories[i])
            if dp[costs[i] + j] >= M:
                result = min(result, costs[i] + j)

print(result)