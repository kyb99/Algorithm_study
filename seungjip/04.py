# 직사각형 널비(2669번)
Testcase = 4
whole_set = set()

for test in range(Testcase):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            whole_set.add((i, j))

print(len(whole_set))