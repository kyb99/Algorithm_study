# 230731
# 방 배정
# 남-남, 여-여, 같은 학년, 한방에 한명 가능
# 최대 인원 K
# 학생수 N

N, K = map(int, input().split())

# w_chart = [[0] for _ in range(7)] # 1~6th grade, index: 1 ~ 6, wo
# 이건 안됨 > 왜?
w_chart = [0 for _ in range(7)] # 1~6th grade, index: 1 ~ 6, wo
m_chart = [0 for _ in range(7)] # 1~6th grade, index: 1 ~ 6, man
rooms = 0

# print(w_chart) # test
for _ in range (N): # N명 만큼 그룹 나누기
    S, Y = input().split() # map(int, ~)
    Y = int(Y)
    # 일단 학년 별로 나누기 / 성별로 나누기
    if S == '0': # women
        w_chart[Y] += 1 # 학년+성별에 인원수 +1 하기
    elif S == '1': # men
        m_chart[Y] += 1

# print(w_chart) # test
# print(m_chart) # test

for students in w_chart: # 각 학년 리스트들, women
    if students != 0:
        if students % K == 0: # 인원수 딱 맞는 경우: 몫만큼
            # print('case1', students // K) # test
            rooms += students // K
        else: # 아닌경우: 몫 + 남은 인원
            # print('case2', students // K +1) # test
            rooms += (students // K) + 1

for students in m_chart: # 각 학년 리스트들, men # debugging > w_chart로 해놨었음
    if students != 0:
        if students % K == 0: # 인원수 딱 맞는 경우: 몫만큼
            # print('case3', students // K) # test
            rooms += students // K
        else: # 아닌경우: 몫 + 남은 인원
            # print('case4', students // K + 1) # test
            rooms += (students // K) + 1

print(rooms)
 
