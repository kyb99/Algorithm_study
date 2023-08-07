# 주말 추가문제

arr = [[0] * 1001 for _ in range(1001)]
T = int(input())

for tc in range(1, T+1):
    j, i, wid, hig = map(int, input().split())
    for y in range(i, i + hig):
        arr[y][j:j+wid] = [tc] * wid


for c in range(1, 1+T):
    count = 0
    for i in range(1001):
        count += arr[i].count(c)
    print(count)