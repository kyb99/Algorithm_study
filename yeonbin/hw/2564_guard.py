# 경비원 # 230823
# 직사각형 모양의 경계를 따라 이동
# 경계에 상점들이 있음
# 동근이의 위치와 각 상점 사이의 최단 거리의 합 구하기
# 1 북, 2 남, 3 서, 4 동
'''
W H 가로 세로
N 상점개수
방향(1~4) 거리 (왼쪽부터 / 위쪽부터)
* N
x y 동근이 위치 좌표
'''

# 꼭지점에서 얼마나 떨어져있는지 확인, 변의 길이 / 상점 거리 확인
# 시계 / 반시계 다 구해보고 최소값?

# 0차이나면(방향 같으면) 둘 사이 거리
# 1 차이:
# 2이상:
# 거리 / (길이-거리) 생각해서 계산해보기

W, H = map(int, input().split())
N = int(input())
shops = [0] * N
for i in range(N):
    shops[i] = tuple(map(int, input().split()))

dir_dong, dist_dong = map(int, input().split())
result = 0
# 더 간단하게 바꿔보자..
for i in range(N):
    dir = shops[i][0]
    dist = shops[i][1]
    if (dir - dir_dong) == 0: # 같은 방위에 위치
        result += abs(shops[i][1] - dist_dong)
    elif dir_dong == 1:
        if dir == 3:
            result += dist_dong
            result += dist
        elif dir == 4:
            result += (W - dist_dong)
            result += dist
        elif dir == 2:
            result += H
            result += min(dist_dong+dist, 2*W-(dist_dong+dist))
    elif dir_dong == 2:
        if dir == 3:
            result += dist_dong
            result += H - dist
        elif dir == 4:
            result += (W - dist_dong)
            result += H - dist
        elif dir == 1:
            result += H
            result += min(dist_dong+dist, 2*W-(dist_dong+dist))
    elif dir_dong == 3:
        if dir == 1:
            result += dist_dong
            result += dist
        elif dir == 2:
            result += (H - dist_dong)
            result += dist
        elif dir == 4:
            result += W
            result += min(dist_dong+dist, 2*H-(dist_dong+dist))
    elif dir_dong == 4:
        if dir == 1:
            result += dist_dong
            result += W - dist
        elif dir == 2:
            result += (H - dist_dong)
            result += W - dist
        elif dir == 3:
            result += W
            result += min(dist_dong+dist, 2*H-(dist_dong+dist))

print(result)

    # 좌표 저장해서 계산하기?
    # x, y = 0
    # dir, dist = map(int, input().split())
    # if dir == 1:
    #     x = dist
    #     y = H
    # elif dir == 2:
    #     x = dist
    #     y = 0
    # elif dir == 3:
    #     x = 0
    #     y = dist
    # else: # dir == 4
    #     x = W
    #     y = dist
    # shops[i] = () # 방향, 거리


# print(shops)
# print(dir_dong, dis_dong)