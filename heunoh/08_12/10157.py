# C x R 좌석이 격자형으로 배정
# 가로, 세로임
# 맨아래 좌석의 번호가 1,1
# 7 x 6 기준 오른위가 7, 6
# 왼쪽아래를 기준으로 대기순서가 k인 관객에게 배정될 좌석 x,y를 찾기
# 실수 두가지
# 1. print(0)을 하고 검사과정을 중단해야함 > 시간초과뜸 > if else로 나눠서
# 2. nameError 마지막 print 를  N - ni로 하면 1일때 ni를 선언한 적이 없기때문에 오류 발생
# > 1일때 조건을 넣어주던가, ni를 i로 수정
import sys
input = sys.stdin.readline
# 입력
M, N = map(int, input().split())
T = int(input())

if N * M < T:
    print(0)
# elif T == 1:
#     print('1 1')
else:
    # 배정할 자리 만들기
    array = [[0] * M for _ in range(N)]
    # 처음에는 1 넣을거니깐
    wait = 1
    # 시작 좌표 설정, 왼쪽 아래가 1,1이니깐 N - i
    i = N - 1
    j = 0
    # k는 델타탐색 리스트를 돌릴 좌표
    k = 0
    # 첫 자리 세팅
    array[i][j] = wait
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    while wait != T:
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 0:
            i = ni
            j = nj
            wait += 1
            array[ni][nj] = wait
        else:
            k += 1
            if k >= 4:
                k = 0
    print(f'{j + 1} {N - i}')
