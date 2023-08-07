# 종이 자르기
# 종이 잘랐을때 가장 큰 종이의 넓이 구하기
'''
입력형식
가로 세로길이(100이하)
N 점선 개수
0/1 점선 *N (가로=0, 세로=1)
'''
# 어떻게 풀어야할까????
# 가장 큰 종이 찾기? 0~자른곳, 자른곳~끝까지 중에 큰거 고르기?
# 이진탐색처럼?
# 아니면 잘라놓고 탐색하면서 칸 수 세기?


import sys
sys.stdin = open('paper_input.txt')


width, height = map(int, input().split())
N = int(input())
# print(width, height, N)
row_cut = [0]
col_cut = [0]
r_cnt = 2 # 가로 자르는 횟수
c_cnt = 2
max_r = 0 # 최대 차 찾기
max_c = 0
for _ in range(N):
    line, cut = map(int, input().split())
    # print(line, cut)
    if line == 0:
        row_cut.append(cut)
        r_cnt += 1
    else:
        col_cut.append(cut)
        c_cnt += 1
row_cut.append(height) # 가로세로 헷갈려서 틀린거임
col_cut.append(width)
row_cut.sort() # return값 반환하는지 잘 보기!
col_cut.sort()
# print(row_cut)
# print(col_cut)
for k in range(r_cnt-1): # 가로 최대 구하기
    tmp = row_cut[k+1] - row_cut[k]
    # print('tmp', tmp)
    if max_r < tmp:
        max_r = tmp
    # print(max_r)
for k in range(c_cnt-1): # 가로 최대 구하기
    tmp = col_cut[k+1] - col_cut[k]
    if max_c < tmp:
        max_c = tmp
    # print(max_c)
print(max_c * max_r)


# for i in range(N):
#     row_s, row_e, col_s, col_e = 0, height-1, 0, width-1
#     line, cut = map(int, input().split())
#     # print(ch, line) # test
#     if line == 0: # row cut
#         if (cut-row_s) < (row_e-cut): # 아래영역이 더 큼
#             row_s = cut
#         else:
#             row_e = cut
#     else: # col cut
#         if (cut-col_s) < (col_e-cut): # 오른쪽이 더 큼
#             col_s = cut
#         else:
#             col_e = cut
#     print(row_s, row_e, col_s, col_e)
# area = (row_e - row_s) * (col_e - col_s)
# print(area)
    
