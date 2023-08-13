# 1244 스위치 켜고 끄기
# 스위치 1 ~
# 0은 꺼짐, 1은 켜짐
# 성별과 받은 수에 따라 스위치 조작
# 남: 스위치가 자기 수의 배수면 스위치 상태 바꿈
# 여: 받은수 위치를 기준으로 좌우 대칭이면서 
# 가장 많은 스위치를 포함하는 구간의 스위치 모두바꿈(홀수 개)

# 출력 초과? 왜 입력 앞에 이상한게 뜨지?
'''
스위치 개수 (1<=N<=100)
처음상태
성별 받은수
(입력 순서대로 바꿈)
>>
스위치 마지막 상태 출력
'''

def ch_switch(switches, idx): # 스위치 상태 바꾸기
    if switches[idx] == 1:
        switches[idx] = 0
    else:
        switches[idx] = 1
    # return 없으면 None반환

N = int(input()) # num of switch
switches = [0] + list(map(int, input().split())) 
# 0번 인덱스에 0 넣어둠 (번호랑 인덱스 맞추려고)

ST = int(input()) # num of students
# print(N, switches, ST) # test
for _ in range(ST):
    s, key = map(int, input().split()) # 성별, 받은 수
    if s == 1: # 남자
        # 배수 바꾸기
        for i in range(key, N, key): # 자기만큼 더하기 == 곱하기
            ch_switch(switches, i)
    elif s == 2: # 여자
        # 대칭 판별해서 구간 바꾸기
        mv = 1 # 주변 조사
        while (0<(key-mv) and (key+mv)<N+1): # 인덱스 범위 벗어나지 않게
            # 대칭이면 mv +1
            if switches[key+mv] == switches[key-mv]:
                ch_switch(switches, key+mv)
                ch_switch(switches, key-mv)
                mv += 1
            # 대칭이 아니면 나온다
            else:
                break
        ch_switch(switches, key) # 가운데 스위치 바꾸기
    # print('ar2', switches) # test
    
# 출력
for i in range(1, N+1):
    print(switches[i], end=' ')
    if (i % 20) == 0: # 20의 배수라면 줄바꿈
        print()