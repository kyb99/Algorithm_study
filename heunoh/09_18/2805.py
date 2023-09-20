# 나무 자르기
#import sys
#input = sys.stdin.readline
# 적어도 M 미터의 나무
N, M = map(int, input().split())
# 20 15 10 17 적어도 M 미터의 나무를 가져가기 위해서 잘라야하는 높이의 최대값
arr = list(map(int, input().split()))

start = 1
end = max(arr)
while start <= end:
    # 자르는 높이
    mid = (start + end) // 2
    # 나무들의 합
    trees = 0
    # 자른 나무들의 합을 구하는 코드
    for i in arr:
        if i > mid:
            trees += (i - mid)
    if trees >= M:
        start = mid + 1
    else:
        end = mid - 1
#print(start)
print(end)