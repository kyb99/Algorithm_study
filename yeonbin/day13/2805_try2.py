# 2805 나무 자르기 # 230918

# 절단기 높이 지정
# 적어도 M미터의 나무를 집에 가져가기 위해 설정할 수 있는 높이의 최대값

# 시간 초과..
# 가운데에서 한번 해보자

# 틀렸음
N, M = map(int, input().split())
trees = list(map(int, input().split()))
total = 0
idx = 0
# 이걸 정렬시켜도 괜찮을까? N (1~1_000_000)
# 일단 ㄱ
trees.sort(reverse=True)
# 제일 높은 나무에서 시작?
# 아니면 가운데에서 시작

def find_h(mid, e, M):
    global h

    total = 0
    # 총합 구하기
    for i in range(mid):
        total += trees[i] - trees[mid]
        h = trees[mid]
    # 마지막 나무
    if e == N-1 and total<M:
        while total < M:
            h -= 1
            total += N
        return
    if total == M:
        return
    elif total > M:
        if (total-mid) < M:
            return
        mid -= 1
        find_h(mid, e, M)
    else:
        mid += 1
        find_h(mid, e, M)

find_h(N//2,N-1,M)


print(h)
