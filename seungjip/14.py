# 10158 개미
N, M = map(int, input().split())
x, y = map(int, input().split())
move = int(input())
x += move
y += move
x %= 2*N
y %= 2*M
if 0 <= x <= N:
    pass
else:
    x = 2*N - x

if 0 <= y <= M:
    pass
else:
    y = 2*M - y

print(x, y)