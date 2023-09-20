# 2805 나무 자르기 # 230918

# 절단기 높이 지정
# 적어도 M미터의 나무를 집에 가져가기 위해 설정할 수 있는 높이의 최대값

# 시간 초과..

N, M = map(int, input().split())
trees = list(map(int, input().split()))
total = 0
idx = 0
# 이걸 정렬시켜도 괜찮을까? N (1~1_000_000)
# 일단 ㄱ
trees.sort(reverse=True)
# 제일 높은 나무에서 시작?
# 아니면 가운데에서 시작?

# 두번째 나무부터 시작
for k in range(1, N):
    h = trees[k]
    idx = k
    total = 0
    # 나무 합 구하기
    for i in range(k):
        total += trees[i] - trees[k]
    # 같거나 크면 나와
    if total >= M:
        break
# 길이가 딱 맞으면
if total == M:
    print(h)
# 길이가 더 길면
elif total > M:
    # 높이 올리기
    while total >= M:
        total -= idx
        h += 1
    print(h-1)
# 길이가 짦으면, 높이를 내려야함
else:
    while total >= M:
        total += N
        h -= 1
    print(h+1)
