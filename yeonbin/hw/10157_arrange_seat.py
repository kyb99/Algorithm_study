# 10157 자리배정 # 230813
# 기다리는 사람들 제일 앞에서부터 1, 2, ...
# (1, 1) 부터 시계방향으로 관객 배정
# 스네일 시계방향
# C, R이 주어질때, K인 관객에게 배정될 좌석번호 (x, y)?
# 해당 관객에게 배정 불가하다면 0 출력
'''
<좌석표 예시> C = 7, R = 6
(1, 6)	 	 	 	 	 	    (7, 6)
 	 	 	 	 	 	 
 	 	 	(4, 4)	 	 	    (7, 4)
(1, 3)	 	 	 	 	(6, 3)	 
(1, 2)	 	 	 	 	 	 
(1, 1)	(2, 1)	(3, 1)	 	 	 (7, 1)
(x, y)
'''
# 델타 탐색으로 가면 되지않을까?
# 1. 배열 > 이걸로 풀었음 > 시간이 엄청 오래걸림 > 어떻게 바꾸지?
# 2. 딕셔너리에 좌표를 넣는다면?
# 델타탐색 할때 for문 순서 어려움..
#  for(4) 이걸 먼저 한다면 방향 4번 바꾸고 끝임! 조심하자!
'''
C R (5 <= C,R <= 1000)
K
>>>
x y
'''
C, R = map(int, input().split())
K = int(input())

# 상 우 하 좌
# dx가 가로이동 임
dx = [0, 1, 0, -1]
dy = [-1, 0, +1, 0]
# all = C*R
if K > C*R:
    print(0)
else:
    # seat = {1:(x, y)} # 이걸로도 해보고싶다
    seat = [[0]*(C) for _ in range(R) ]
    x = 0 # 가로
    y = R - 1 # 세로
    seat[y][x] = 1
    num = 2 # 1은 이미 넣어 놨으니까
    # 조사는 K 까지만 하면 됨.. 근데..어케하는지 몰라서 내맘대로
    while num < K+1:
        for i in range(4): # 4 dirction
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<= nx < C and 0 <= ny < R and seat[ny][nx] == 0 and num <= K:
                seat[ny][nx] = num
                # print('nx, ny', nx, ny, 'num', num)
                x, y = nx, ny
                num += 1
                nx = x + dx[i]
                ny = y + dy[i]
            if num > K: # for 문 나오기
                break

    # for i in range(R):
    #     for j in range(C):
    #         print(seat[i][j], end=' ')
    #     print()
    print(x+1, R-y)
