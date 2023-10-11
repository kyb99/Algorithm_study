# 평범한 배낭 # 230929
# N개의 물건, 무게 W, 가치 V
# 배낭 K, 가치의 최댓값?

# 어떻게 풀지?
# dp?


N, K = map(int, input().split())
# W V
arr = [list(map(int, input().split())) for _ in range(N)]
value = [0]*(N+1)
