# 위치옮기기
import sys
input = sys.stdin.readline
W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
result_x = 0
result_y = 0
a = (x + t) // W
b = (y + t) // H

if a % 2 == 0:
    result_x = (x + t) % W
else:
    result_x = W - (x + t) % W

if b % 2 == 0:
    result_y = (y + t) % H
else:
    result_y = H - (y + t) % H

print(f'{result_x} {result_y}')