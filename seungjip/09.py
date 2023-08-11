# 빙고(2578번)
import sys
sys.stdin = open("a.txt")

# 모든 함수들은 2중배열과 점의 좌표를 넣었을때 리턴값은 1로 하여 나중에 count에 더할 것
# 어떤 점을 기준으로 가로가 빙고인지 확인하는 함수(2중, 고정행 인덱스)
def check_row(Board, i):
    mid = 0
    for l in range(5):
        mid += Board[i][l]
    if mid == -5:
        return 1
    else:
        return 0

# 어떤 점을 기준으로 세로가 빙고인지 확인하는 함수(2중, 고정열 인덱스)
def check_col(Board, j):
    mid = 0
    for l in range(5):
        mid += Board[l][j]
    if mid == -5:
        return 1
    else:
        return 0

# 어떤 점이 대각선 위인 경우 확인하는 함수(2중, /  -> 0 또는 \ -> 1)
def check_x(Board,dir):
    mid = 0
    if dir == 0:
        for l in range(5):
           mid += Board[l][l]
        if mid == -5:
            return 1
        else:
            return 0
    else:
        for l in range(5):
            mid += Board[l][4-l]
        if mid == -5:
            return 1
        else:
            return 0

# 정중앙이면 위의 세 함수 돌면 됨

Board = [list(map(int, input().split())) for _ in range(5)]
ho_list = []
count = 0
for _ in range(5):
    ho_list += list(map(int, input().split()))

for i in range(len(ho_list)):
    # 사회자가 하나씩 부를 때 마다 리스트를 순회하며 그 친구를 찾아서 값을 -1로 바꿈
    a, b = 0, 0
    for j in range(5):
        for k in range(5):
            if Board[j][k] == ho_list[i]:
                Board[j][k] = -1
                a = j
                b = k
    # 위치에 따라 (정중앙(1), 대각선 위(8), 나머지(16))
    # 정중앙의 경우 4가지 case(가로, 세로, 대각 2개)
    # 대각선 위의 경우 3가지 case (가로, 세로, 그 대각 1개)
    # 나머지 2가지 case(가로, 세로)

    if a==2 and b==2:
        count += check_x(Board, 0)
        count += check_x(Board, 1)
        count += check_row(Board, a)
        count += check_col(Board, b)
    elif a == b:
        count += check_x(Board, 0)
        count += check_row(Board, a)
        count += check_col(Board, b)
    elif a == 4-b:
        count += check_x(Board, 1)
        count += check_row(Board, a)
        count += check_col(Board, b)
    else:
        count += check_row(Board, a)
        count += check_col(Board, b)

    if count >= 3:
        print(i+1)
        break