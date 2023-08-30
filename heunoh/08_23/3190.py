# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())
arr = [[0] * N for _ in range(N)]
# 방향을 지시할 리스트
move = []

def is_valid(i,j):
    return 0 <= i < N and 0 <= j < N
# a는 지금 방향
# 리턴하는 숫자가 바뀔 델타탐색의 인덱스
def change_dir(a, c_dir):
    # 오른쪽으로 갈떄 왼쪽90 오른쪽 90
    if a == 0:
        if c_dir[1] == 'D':
            return 1
        if c_dir[1] == 'L':
            return 3
    elif a == 1:
        if c_dir[1] == 'D':
            return 2
        if c_dir[1] == 'L':
            return 0
    elif a == 2:
        if c_dir[1] == 'D':
            return 3
        if c_dir[1] == 'L':
            return 1
    elif a == 3:
        if c_dir[1] == 'D':
            return 0
        if c_dir[1] == 'L':
            return 2

# 오른쪽 아래 왼쪽 위
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 처음에는 오른쪽으로
# 사과를 넣어주는 과정
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 5
# 뱀은 1로 표현
snail_pos = [0, 0]
arr[snail_pos[0]][snail_pos[1]] = 1
snail = []
snail.append(snail_pos)
# 방향 변환 횟수
L = int(input())
for _ in range(L):
    t = list(input().split())
    move.append(t)
i = 0
j = 0
time_count = 0
snail_dir = 0
#print(move)
while True:
    time_count += 1
    ni = i + di[snail_dir]
    nj = j + dj[snail_dir]


    # if is_valid(ni, nj) and arr[ni][nj] == 0:
    #     arr[ni][nj] = 1
    #     delete = snail.pop(0)
    #     arr[delete[0]][delete[1]] = 0
    #     snail.append([ni, nj])
    #     for i in arr:
    #         print(i)
    #     print('-------', time_count)
    #     print(ni, nj)
    # elif is_valid(ni, nj) and arr[ni][nj] == 5:
    #     snail.append([ni, nj])
    #     arr[ni][nj] = 1
    #     for i in arr:
    #         print(i)
    #     print('-------', time_count)
    #     print(ni, nj)
    if len(move) >= 1 and time_count == int(move[0][0]):
        # tmp는 시간이랑 방향이 들어있는 리스트
        tmp = move.pop(0)
        snail_dir = change_dir(snail_dir, tmp)
        # for i in arr:
        #     print(i)
        # print(ni, nj)
        # print('---c----', time_count)

    if is_valid(ni, nj) and arr[ni][nj] == 5:
        snail.append([ni, nj])
        arr[ni][nj] = 1
        # for i in arr:
        #     print(i)
        # print('-------', time_count)
        # print(ni, nj)
    elif is_valid(ni, nj) and arr[ni][nj] == 0:
        arr[ni][nj] = 1
        delete = snail.pop(0)
        arr[delete[0]][delete[1]] = 0
        snail.append([ni, nj])
        # for i in arr:
        #     print(i)
        # print('-------', time_count)
        # print(ni, nj)
    else:
    #if not is_valid(ni, nj) or arr[ni][nj] == 1:
        print(time_count)
        break
    # if len(move) >= 1 and time_count == int(move[0][0]):
    #     # tmp는 시간이랑 방향이 들어있는 리스트
    #     tmp = move.pop(0)
    #     snail_dir = change_dir(snail_dir, tmp)
    #     for i in arr:
    #         print(i)
    #     print(ni, nj)
    #     print('---c----', time_count)
    i, j = ni, nj
