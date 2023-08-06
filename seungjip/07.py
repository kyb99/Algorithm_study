# 색종이(2563번)
Testcase = int(input())
square = set()

for test in range(Testcase):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            square.add((i, j))

print(len(square))