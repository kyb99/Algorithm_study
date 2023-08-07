# 빙고
# 사회자가 몇번째 수를 부른 후 빙고인지?
# 빙고는 3줄이상일때
# 5*5

# 어려웠던점: 숫자를 찾고 for문 두개 나가기, 배열이름, 


import sys
sys.stdin = open('bingo_input.txt')

def check_bingo(arr):
    bing = 0 # 줄개수
    for i in range(5): # 가로
        cnt = 0
        for j in range(5):
            if arr[i][j] == -1:
                cnt += 1
        if cnt == 5:
            bing += 1
    for j in range(5): # 세로
        cnt = 0
        for i in range(5):
            if arr[i][j] == -1:
                cnt += 1
        if cnt == 5:
            bing += 1
    cnt = 0
    cnt2 = 0
    for i in range(5): # 대각
        if arr[i][i] == -1:
            cnt += 1
        if arr[i][4-i] == -1:
            cnt2 += 1
    if cnt == 5:
        bing += 1
    if cnt2 == 5:
        bing += 1
    return bing



arr = [list(map(int, input().split())) for _ in range(5)] # bingo board
call = [] # 사회자가 부르는 숫자
ans = 0 # 몇번째 수인지
bing = 0 # 빙고개수

for _ in range(5):
    call += list(map(int, input().split())) # 리스트 더하기
# print(call)
for idx in range(25): # 사회자 숫자 순회
    nxt = False # 숫자 찾았는지 확인하는 용
    for i in range(5):
        for j in range(5):
            # print(i, j, end='  ')
            if arr[i][j] == call[idx]:
                # print('aa', i, j)
                arr[i][j] = -1 # 부르는 숫자 -1로 바꾸기
                bing = check_bingo(arr)
                if bing >= 3:
                    ans = idx + 1 # 인덱스가 0부터니까
                nxt = True
                break # 찾으면 다음 숫자 바로 찾게 넘어가고싶다면?
        if  nxt == True:
            break
    if bing >= 3:
        break
print(ans) # 몇번째에 불렀는지 출력

