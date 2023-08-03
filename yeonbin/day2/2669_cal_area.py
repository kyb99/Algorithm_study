# 직사각형 네개의 합집합의 면적 구하기 #230802 #1648~1706
# 축에 평행한 직사각형 4개, 얘네가 차지하는 면적 구하기
# 겹쳐있을 수도, 포함할수도, 떨어져있을수도
# 1<=x,y<=100

# 오늘 한거랑 비슷한 내용인듯
# 100 x 100 배열 만들고, 1이상인 곳만 면적세기
# x, y좌표 반대, 위아래도 반대지만 노상관
# 더 나은코드로 만들어보자?

arr = [[0]*101 for _ in range(101)] 
# x,y가 100까지라서 그냥 101로 함. 인덱스범위 모르겠어서
area = 0 # 구할 면적

for _ in range(4): # 4 rectangles
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1
     # 사각형 만큼 칠하기

# test
# for i in range(0,10):
#     for j in range(0, 10):
#         print(arr[i][j], end=' ')
#     print()
#            

for i in range(0,101):
    for j in range(0, 101):
        if arr[i][j] > 0:
            area += 1 
# 배열 돌면서 면적 계산하기
print(area)

