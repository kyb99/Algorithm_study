import sys
sys.setrecursionlimit(10**9)
K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
res = -1

def get_num(point):
    tmp = 0
    for i in arr:
        tmp += i // point
    return tmp

start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

print(end)