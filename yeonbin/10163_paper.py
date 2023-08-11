# 색종이 # 230807
# 순서대로 놓는거라 앞에 놓인게 가리는거임
# 맨 마지막꺼는 하나도 안가리겠지, 문제 잘 읽기
# 현재 53점 왜? 메모리 초과!
'''
입력형식
- N (1~100)
- 색종이에 관한 입력 *N
(왼쪽칸 번호, 너비, 높이)
- 좌표
(0,3)   (1,)    (2,)
(0,2)   (1,)    (2,)
(0,1)   (1,)    (2,)
(0,0)   (1,)    (2,)

출력형식
입력 순서대로 각 색종이가 보이는 부분 면적
안보이면 0
'''
# 칸이 위아래가 다르네? 상관없을듯, 걍 맞기만 하면됨..ㅎ
# 경계밖으로 나가는 경우 없음
# 주어진 값이 오른쪽 위라고 생각하자
# set 만들어서 차집합 ㄱ ?

N = int(input())
area = list() # 색종이들 모음
for _ in range(N): # N번 만큼 색종이 입력 받음
    x, y, width, height = map(int, input().split())
    # 좌표 넣을 세트
    p_set = set()
    for i in range(x, x+width): # 가로
        for j in range(y, y+height): # 세로
            p_set.add((j, i))
    area.append(p_set)
for target in range(N-1): # 교집합 구해서 빼기
    tmp = set() # 교집합 넣을 세트
    for diff in range(target+1, N):
        tmp = tmp.union(area[target] & area[diff]) # 교집합을 세트에 넣어줌
        # union 쓸때 반환값이 집합이니까 변수에 할당해야함!
        # print('gyo ar', len(tmp))
    print(len(area[target] - tmp)) # 0~N-2까지 색종이영역 출력
print(len(area[N-1])) # 마지막 색종이 영역 출력

    




# 이렇게도 가능할듯?
# for _ in range(N): # 색종이 입력받기
#     info = list(map(int, input().split()))
#     print(info) # test
#     p_set = set()
#     for i in range(info[0], info[0]+info[2]):
#         for j in range(info[1], info[1]+info[3]):
#             pass


