# 5x5 배열
bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]
# bingo 의 원소와 check 의 원소를 비교하고 만약 빙고가 나오면 몇번째 수를 불럿는지를 출력
# 가로, 세로 대각선을 비교
# 부른값을 찾아서 0으로 만들고 각 줄의 합이 0이되면 빙고를 카운트
def check_bingo(arr):
    count = 0

    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += arr[i][j]
        if tmp == -5:
            count += 1

    for j in range(5):
        tmp = 0
        for i in range(5):
            tmp += arr[i][j]
        if tmp == -5:
            count += 1

    di = [1, -1]
    dj = [1, 1]

    tmp = 0
    for i in range(5):
        tmp += arr[di[0]*i][dj[0]*i]
        if tmp == -5:
            count += 1
    tmp = 0
    for i in range(5):
        tmp += arr[4 + (di[1]*i)][dj[1] * i]
        if tmp == -5:
            count += 1

    if count == 3:
        return True
    else:
        return False
idx = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for m in range(5):
                if bingo[k][m] == check[i][j]:
                    bingo[k][m] = -1
                    idx += 1
    if check_bingo(bingo):
        print(idx)
        break

