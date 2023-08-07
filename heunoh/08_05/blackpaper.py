from pprint import pprint
paper = int(input())
# 종이의 크기는 10x10
di = 10
dj = 10
# 검은 부분을 셀 변수
count = 0
# 100x100 그리드 생성
grid = [[0] * 100 for _ in range(100)]
# 몇장 붙일래
for tc in range(paper):
    M, N = map(int, input().split())

    for i in range(N, N+di):
        grid[i][M:M+dj] = [1]*dj
        
for i in range(100):
    for j in range(100):
        if grid[i][j] != 0:
            count += 1
print(count)
