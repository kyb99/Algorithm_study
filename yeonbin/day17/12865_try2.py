# 평범한 배낭 # 230929
# N개의 물건, 무게 W, 가치 V
# 배낭 K, 가치의 최댓값?

# 어떻게 풀지? 비트마스킹? 이것도 시간초과

N, K = map(int, input().split())
# W V
arr = [list(map(int, input().split())) for _ in range(N)]

val = 0
acc = 0
max_v = 0
is_pos = True

# for i in range(1, 1<<N):
#     for j in range(N):
#         if (i & (1<<j)):
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()

for i in range(1, 1<<N):
    acc, val = 0, 0
    is_pos = True
    for j in range(N):
        if (i & (1<<j)):
            # 사용
            val += arr[j][1]
            acc += arr[j][0]
        else:
            # 사용안함
            continue
        if acc > K:
            is_pos = False
            break
    #
    if is_pos==True and max_v < val:
        max_v = val
print(max_v)