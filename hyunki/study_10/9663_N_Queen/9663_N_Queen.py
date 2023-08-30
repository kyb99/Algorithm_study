import sys
sys.stdin = open('input.txt')

# N x N 인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓을 수 있는 경우의 수
# queen은 가로,세로, 대각선 다 이동 가능
# Q기준으로 2칸 전진 1칸 아래는 잡을 수 없다(나이트 위치)


N = int(input())

# 체스판 생성
chess = [[0] * N for _ in range(N)]

# (0,0)부터 순회하면서 첫번째 퀸을 놓고 그 기준을 기점으로 경우의 수 생각
for x in range(N):
    for y in range(N):
        chess[x][y] = 1 # 기준 퀸 생성

        # 모든 위치 다 찰때까지 반복
        while True:

