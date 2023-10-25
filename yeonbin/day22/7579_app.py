# 앱 # 231025
# M 바이트 이상의 메모리를 확보해야함
# 비용의 합을 최소화하여 확보
# 최소 비용 출력

N, M = map(int, input().split())
memories = [0]+list(map(int, input().split()))
costs = [0]+list(map(int, input().split()))

max_memo = sum(memories)

# 어떻게 풀지? 냅색 알고리즘인데..?
# 최소비용 저장..
# 쓴다 안쓴다.. 언제 안쓰지?
# M 이상이어야하는데...어렵군...

# 1차원으로 하려고 했는데 어렵다..!
# dp = [-1] * (max_memo+1)
# dp[0] = 0

# for j in range(N):
#     for i in range(max_memo+1): # 최소 구하는거니까 처음부터
#         # 조사 범위 벗어난 경우
#         if memories[j] + i > max_memo:
#             continue

# 2차원 ㄱㄱ
dp = [[-1]*(N+1) for _ in range(max_memo)]
dp = [[0]*(N+1)] + dp
print(dp)
result = 1e9
for j in range(N+1):
    for i in range(1, max_memo+1):
        if i-memories[j] < 0:
            continue
        elif dp[i-memories[j]][j-1] == -1:
            continue
        else:
            dp[i][j] = max(dp[i-memories[j]][j-1] + costs[j], dp[i][j-1])
            # min으로 하면..안쓰니까..
            if i >= M:
                dp[i][j] = min(dp[i-memories[j]][j-1] + costs[j], dp[i][j-1])
                result = min(result, dp[i][j])
# print(dp[M:])
print(result)
'''
      30 10 20 35 40
   0  1  2  3  4  5
0  0  0  0  0  0  0
10 -1  -1 0  0  0  0
20 -1 -1 -1 3  3  3
30 -1 3* 3  3* 3  3
35 -1 -1 -1 -1 4* 4
40 .  -1 3* 3  3  3 
45 .        -1 5* 
50 .
55 .
60 .
65 .
75 .
80 .
85 .
'''