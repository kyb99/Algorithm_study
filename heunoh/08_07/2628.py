# 3번째 줄 이후의 입력값의 첫 값이 0이면 가로로
# 1이면 세로로 가르기
# 가로, 세로
M, N = map(int, input().split())
T = int(input())
# T번만큼 받아올것
cut_position = [list(map(int, input().split())) for _ in range(T)]
# 세로 > position 기준으로 j를 자름
# 가로 > position 기준으로 i를 자름
# 여러번 자르면 0 ~ 2 / 2 ~ 3 / 2~ 7 이렇게 나뉨
# 구간을 대소를 구분해서 나눈것이 좋아보임
#print(cut_position)
# cut_position = [[0,2],[0,3],[1.4]]
cut_i = [0, N]
cut_j = [0, M]
for num in cut_position:
    if num[0] == 0:
        cut_i.append(num[1])
    else:
        cut_j.append(num[1])
# 범위를 받아오고 정렬
cut_i.sort()
cut_j.sort()
#print(cut_i, cut_j)

max_i = 0
max_j = 0

for i in range(1, len(cut_i)):
    tmp = cut_i[i] - cut_i[i-1]
    if max_i < tmp:
        max_i = tmp

for j in range(1, len(cut_j)):
    tmp = cut_j[j] - cut_j[j-1]
    if max_j < tmp:
        max_j = tmp

print(max_i*max_j)

