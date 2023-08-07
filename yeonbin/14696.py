# 딱지놀이 # 230807
# 만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
# 별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
# 별=4, 동=3, 네=2, 세 =1
'''
입력
N : rounds
a 1 1 4 ... :a개 + 딱지 종류
b 2 2 .. :그림 b개 + 딱지 종류
'''
def winner(a_count, b_count):
    for i in range(4, 0, -1):
        if a_count[i] < b_count[i]:
            return 'B'
        elif a_count[i] > b_count[i]:
            return 'A'
    return 'D'

# 카운팅 정렬
N = int(input())
for _ in range(N):
    NA, *a = map(int, input().split()) # 개수, 종류
    NB, *b = map(int, input().split())
    # 딱지 종류 개수 셀 리스트 만들기(1 ~ 4니까 5개 만들기)
    a_count = [0] * 5
    b_count = [0] * 5

    for dd in a:
        a_count[dd] += 1 # 해당 인덱스 칸에 +1
    for dd in b:
        b_count[dd] += 1  # 해당 인덱스 칸에 +1

    print(winner(a_count, b_count))

    # 이렇게 노가다로 말고 잘 푸는 법은 없나? 함수로?
    # if a_count[4] > b_count[4]:
    #     result = 'A'
    # elif a_count[4] < b_count[4]:
    #     result = 'B'
    # else: # draw 4
    #     if a_count[3] > b_count[3]:
    #         result = 'A'
    #     elif a_count[3] < b_count[3]:
    #         result = 'B'

