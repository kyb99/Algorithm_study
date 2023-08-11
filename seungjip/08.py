# 종이 자르기(2628 번)
M, N = map(int, input().split())
cutting = int(input())
width = [0, M]
height = [0, N]
for cut in range(cutting):
    direction, line = map(int, input().split())
    if direction == 0:
        height.append(line)
        height.sort()

    else:
        width.append(line)
        width.sort()

max_width = 0
max_height = 0

for i in range(len(width)-1):
    div = width[i+1] - width[i]
    if max_width <= div:
        max_width = div

for j in range(len(height)-1):
    div = height[j+1] - height[j]
    if max_height <= div:
        max_height = div
print(max_height*max_width)