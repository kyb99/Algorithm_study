# 주사위 쌓기
# 아래에서부터 1, 2, 3, ..순으로 쌓기
# 아래 주사위의 윗면 = 위 주사위의 아랫면 숫자
# 사각기둥 - 옆면의 합이 최대가 되도록
# 한 옆면의 숫자 합의 최댓값 구하기
'''
5 주사위 개수
2 3 1 6 5 4 주사위 종류 (A B C D E F)
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3

A-F, B-D, C-E가 서로 마주보는 면
'''

# 1~6까지는 전부 있으니까 1을 맨 밑으로 하면 되지 않을까?
# 아니면 옆면이 6이 되도록?
# 하나씩 다 해보기?
# 밑 / 위가 6이면 +5, 아니면 +6 하면 되지않나? 함수 만들어서 + 딕셔너리?

# (0,5) (1, 3) (2, 4) 번째가 서로 마주봄

N = int(input()) # 주사위 개수
partner = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
cnt = 0
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))
    # print(dice)
# 모르겠다...
        
    
print(cnt)
    


# one = 0 # 1의 인덱스
    # 잘못생각했음
    # for i in range (6):
    #     if dice[i] == 1:
    #         one = i
    #         break
    # if one == 0:
    #     if dice[5] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6
    # elif one == 1:
    #     if dice[3] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6
    # elif one == 2:
    #     if dice[4] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6
    # elif one == 3:
    #     if dice[1] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6
    # elif i == 4:
    #     if dice[2] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6
    # elif one == 5:
    #     if dice[0] == 6:
    #         cnt += 5
    #     else:
    #         cnt += 6