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
        #print(i)
        tmp += i // point
        #print(tmp)
    return tmp
def binary(start,end):
    global res
    mid = (start + end) // 2
    if start > end:
        return
    num = get_num(mid)
    if num > N:
        res = max(res, mid)
        binary(mid, end)
    elif num < N:
        binary(start, mid)
    else:
        res = max(res, mid)

#print(get_num(200))
binary(0, max(arr))
print(res)