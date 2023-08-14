# 10158 개미 #230814

'''
w h 가로 세로
p q 초기 위치 좌표
t 움직일 시간

왼쪽 아래가 (0,0)
'''

# 1. delta
# row, col 순서 (-1,1), (-1, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)
# 2. 수학으로..

col, row = map(int, input().split())
x, y = map(int, input().split())