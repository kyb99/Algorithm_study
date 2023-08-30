# import sys
# sys.stdin = open('input.txt')

T = int(input())
arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))

# A,B,C,D,E,F 순으로 입력
# A-F (1,6), B-D (2,4) , C-E(3,5) 연결
# 맨 아래에 가장작은값이 오도록..?

def get_side(bottom, top, arr):
    tmp = []
    for i in range(6):
        if i == bottom or i == top:
            continue
        else:
            tmp.append(arr[i])
    side_arr.append(tmp)

# 상대되는 인덱스를 전달
def get_top(bottom):
    if bottom == 0:
        return 5
    elif bottom == 1:
        return 3
    elif bottom == 2:
        return 4
    elif bottom == 3:
        return 1
    elif bottom == 4:
        return 2
    elif bottom == 5:
        return 0
#print(arr)
max_val = 0
for i in range(6):
    side_arr = []
    tmp = 0
    bottom = i
    top = get_top(bottom)
    get_side(bottom, top, arr[0])
    #print(f'bottom : {bottom}, top : {top}')
    for j in range(1, T):
        bottom = arr[j].index(arr[j-1][top])
        top = get_top(bottom)
        get_side(bottom, top, arr[j])
        #print(f'bottom : {bottom}, top : {top}')
    for side in side_arr:
        tmp += max(side)

    if tmp > max_val:
        max_val = tmp
    #print(side_arr)
print(max_val)
