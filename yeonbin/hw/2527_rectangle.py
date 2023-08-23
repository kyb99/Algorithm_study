# 직사각형 # 230822 ~ 230823
# x, y 왼쪽 아래, p,q 오른쪽 위 꼭짓점
# 두 직사각형의 공통부분을 조사해서 해당하는 코드 문자를 출력
# 직사각형 a, 선분 b, 점 c, 공통부분 없음 d
'''
3 10 50 60 100 100 200 300 (x1, y1, p1, q1, x2, y2, p2, q2)
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

# 직사각형 영역 사이에 꼭짓점이 들어있으면 직사각형
# 선분: x1<x2<p1, y1 == q2 / y2 == q1 / 세로 두가지 경우도 있음
# 점인 경우: (p1,y1) == (x2,q2) / 4가지 경우가 있음 *2
# 범위를 아예 벗어난 경우
# 모든 경우를 다 나눠보자
def find_ans(x1, y1, p1, q1, x2, y2, p2, q2):
    # 겹치지 않는 경우
    if p1 < x2 or p2 < x1 or y1 > q2 or y2 > q1:
        return 'd'
    # 점
    elif (x2, y2) == (p1, q1) or (x1, y1) == (p2, q2):
        return 'c'
    elif (x1, q1) == (p2, y2) or (x2, q2) == (p1, y1):
        return 'c'
    # 선분
    elif y1 == q2 and (x1 <= x2 < p1 or x1 < p2 <= p1 or x2 <= x1 < p2 or x2 < p1 <= p2): # 바닥면 선분
        return 'b'
    elif q1 == y2 and (x1 <= x2 < p1 or x1 < p2 <= p1 or x2 <= x1 < p2 or x2 < p1 <= p2): # 윗면
        return 'b'
    elif p1 == x2 and (y1 <= y2 < q1 or y1 < y2 <= q1 or y2 <= y1 < q2 or y2 < y1 <= q2): # 오른쪽
        return 'b'
    elif p2 == x1 and (y1 <= y2 < q1 or y1 < y2 <= q1 or y2 <= y1 < q2 or y2 < y1 <= q2): # left
        return 'b'
    # 직사각형
    else:
        return 'a'

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    ans = find_ans(x1, y1, p1, q1, x2, y2, p2, q2)
    # print(x1, y1, p1, q1, x2, y2, p2, q2)
    print(ans)
