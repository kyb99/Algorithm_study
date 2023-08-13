# 색종이 230807
# 색종이가 붙은 영역의 넓이 구하기
# 색종이는 항상 10*10
# set 이용? 중복생각 안해도 되니까
N = int(input())
colored = set()
for _ in range(N):
    x, y = map(int, input().split()) # 왼, 아
    for i in range(10): # 가로
        for j in range(10): # 세로
            colored.add((x+i, y+j)) # 해당 좌표 집합에 넣기
print(len(colored))
