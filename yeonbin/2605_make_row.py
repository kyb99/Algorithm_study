# 줄세우기 #230802 # 시간: 1521~1536
# 첫번째 0
# 두번 : 0 / 1
# .. 뽑은 숫자만큼 앞으로 가서 줄서기
# 학생들의 최종 줄 선 순서 출력

# for문 쓰면 될듯?

N = int(input()) # students
moves = list(map(int, input().split()))
# row = [1] # 이렇게하면 도는걸 1부터 하면됨
row = []
for i in range(N): # moves 리스트 안에 있는걸 돌거임
    row.insert(len(row)-moves[i], i+1) # i+1은 학생번호
    # 0 뽑으면 맨 뒤고, 1이면 한칸 앞이니까
print(*row)

# 빈리스트로 시작해도 되네