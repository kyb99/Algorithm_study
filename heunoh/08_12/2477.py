# 참외밭
# 참외의 개수
import sys
input = sys.stdin.readline

T = int(input())
dir_arr = []
len_arr = []
hig_arr = []
wid_arr = []
small_len = []
def check_dir(a, b):
    if a == 1 or a == 2:
        wid_arr.append(b)
    else:
        hig_arr.append(b)

for _ in range(6):
    a, b = map(int, input().split())
    check_dir(a, b)
    dir_arr.append(a)
    len_arr.append(b)

for i in range(6):
    if dir_arr[i] == dir_arr[(i+2) % 6]:
        small_len.append(len_arr[(i+1) % 6])

small_area = small_len[0] * small_len[1]

big_area = max(hig_arr) * max(wid_arr)
#print(big_area)

result = (big_area - small_area) * T
print(result)

