# 나무 자르기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# 20 15 10 17 적어도 M미터의 나무를 가져가기 위해서 잘라야하는 높이의 최대값
arr = list(map(int, input().split()))
candidate = []

# 초기 start 는 0으로  end 는 가장 높은 나무의 높이로

def get_sum(point):
    tmp = 0
    for i in arr:
        to_add = i - point
        if to_add > 0:
            tmp += to_add
    return tmp


def binary(start, end):
    mid = (start + end) // 2
    trees = get_sum(mid)
    if start > end:
        return
    # 합이 작으면
    if trees < M:
        binary(start, mid)
    elif trees > M:
        candidate.append(mid)
        binary(mid, end)
    else:
        candidate.append(mid)

first_end = max(arr)
binary(0, first_end)
print(max(candidate))