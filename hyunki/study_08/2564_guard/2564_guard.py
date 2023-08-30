import sys
sys.stdin = open('input.txt')

def distance(loc, dis):
    if loc == 1:
        return dis
    elif loc == 4:
        return v + dis
    elif loc == 2:
        return v + h + v - dis
    elif loc == 3:
        return v + h + v + h - dis

v, h = map(int, input().split())
N = int(input())
store = []
for i in range(N+1):
    loc, dis = map(int, input().split())
    store.append(distance(loc, dis))

start = store[-1]

result = 0

for i in range(N):
    cal_distance = abs(store[i] - start)

    total = 2 * (v + h)

    result += min(cal_distance, total - cal_distance)

print(result)