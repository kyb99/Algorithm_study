import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
active_list = [0] + list(map(int, input().split()))
cost_list = [0] + list(map(int, input().split()))

# 코스트 최대값
high = sum(cost_list) + 1

# 냅색 알고리즘
# -> dp[i][j] = i번째 앱까지 비용 j로 얻을 수 있는 최대 메모리
dp = [[0 for _ in range(high)] for _ in range(N + 1)]

result = sys.maxsize

for i in range(1, N + 1):
    active = active_list[i]
    cost = cost_list[i]

    for j in range(high):
        # cost가 j를 넘어가면 종료를 못시키니깐 이전값 가져오기
        if cost > j:
            dp[i][j] = dp[i - 1][j]
        # cost가 j보다 작거나 같으면 종료 시킨다.
        # 앱을 종료 안했을 때와 종료했을 때 최대값 비교
        else:
            dp[i][j] = max(active + dp[i - 1][j - cost], dp[i - 1][j])

        # 확보한 메모리 크기가 M을 넘으면
        if dp[i][j] >= M:
            result = min(result, j)

print(result)
