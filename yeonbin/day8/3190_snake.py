# 뱀 # 230823
# N*N 보드
# 시작: 맨위 맨 좌측 > 오른쪽
# 뱀 길이 1
# 규칙
# 1. 몸길이늘려 머리를 다음칸에
# 2. 벽 / 자기몸이랑 부딪히면 게임끝
# 3. 이동한 칸에 사과가 있으면 사과 없어지고 꼬리 안없어짐
# 4. 사과 없으면 몸길이 줄여서 꼬리칸 비우기
# 위치 + 이동 경로 > 몇초에 끝나는지 계산

'''
N 보드크기
K 사과 개수
사과 위치(행 열)
*K
L 방향변환 횟수
방향변환 정보(몇초 뒤에 90도 회전)
X L/D
'''

def pprint(List):
    for i in List:
        for j in i:
            print(j, end=' ')
        print()
# 해결못함

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
# 사과 위치 1로 표시
for _ in range(K): # (1,1부터 시작하니까 여기선 -1씩 해줘야함)
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

L = int(input())
dir_list = [[0, 0] for _ in range(L+1)]
for i in range(L):
    t, dir = input().split()
    dir_list[i+1] = [int(t), dir] # t, dir
    # dir == 'L'이면 왼, 'D'면 오

pprint(board)
# 초기 위치
i = 0
j = 0
end_i = 0
end_j = 0
# 뱀 몸통을 2로 표시
board[i][j] = 2
game_over = False
time = 1
# 이거 델타탐색으로?
# 오 하 좌 우 (오른쪽으로 도는거)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 처음엔 오른쪽으로 직진
k = 0
print(dir_list) #t
while not game_over:
    for turn in range(1, L+1): # 턴 횟수만큼
        # print('t', turn[0]) # t
        for mv in range(dir_list[turn][0] - dir_list[turn-1][0]):
            print('time', time) # t
            ni = i + di[k]
            nj = j + dj[k]
            # print('ni, nj', ni, nj)
            if (0<=ni<N and 0<=nj<N): # 벽에 안부딪히면
                if board[ni][nj] == 2:
                    # 게임오버
                    print('gg') #t
                    game_over = True
                    break
                elif board[ni][nj] == 1:
                    # 사과
                    board[ni][nj] = 2
                else: # 그냥 가는경우
                    board[ni][nj] = 2 # 머리 한칸 이동
                    for dk in range(4): # 델타탐색해서 꼬리 땡기기...여기가 문제다.
                        end_ni, end_nj = end_i+di[dk], end_j+dj[dk]
                        if 0<=end_i<N and 0<=end_j<N:
                            if board[end_ni][end_nj] == 2:
                                board[end_i][end_j] = 0
                                end_i, end_j = end_ni, end_nj
                    
                i, j = ni, nj # 머리 위치 바꿔주기
                time += 1
            else: # 범위 벗어나면(벽에 부딪히면)
                # 게임오버
                game_over = True
                break
        # 여기까지가 턴 하기전에 직진하는거
            pprint(board) # t

        if game_over:
            break
        if dir_list[turn][1] == 'L':
            # 왼쪽으로 턴
            k += -1
        elif dir_list[turn][1] == 'D':
            # 오른쪽으로 턴
            k += 1
        k = k % 4 # 4의 나머지로! 더 커지면 범위 벗어남
        print('k', k) # t
    else: # 방향전환이 끝나면
        if (0<=ni<N and 0<=ni<N):
            if board[ni][nj] == 2:
                # 게임오버
                game_over = True
                break
            elif board[ni][nj] == 1:
                # 사과
                board[ni][nj] = 2
            else:
                board[ni][nj] = 2
                board[i][j] = 0 # 꼬리 땡기기
            i, j = ni, nj # 머리 위치 바꿔주기
            time += 1
        else:
            # 게임오버
            game_over = True
            break

print(time)
# print(board)
