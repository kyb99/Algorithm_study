# 색종이(10163번)

Testcase = int(input())
set_list = []
for test in range(1, Testcase + 1):
    x, y, xr, yr = map(int, input().split())
    each_set = set()
    for i in range(x, x+xr):
        for j in range(y, y+yr):
            each_set.add((i,j))
    set_list.append(each_set)


for i in range(len(set_list)-1):
    dis_list = set_list[i+1:]
    A = set_list[i]
    for j in dis_list:
        A = A-j
    print(len(A))
print(len(set_list[-1]))