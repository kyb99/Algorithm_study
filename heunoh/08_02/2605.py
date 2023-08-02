# 줄세우기
# 08_02 study
T = int(input())
i = list(map(int, input().split()))
# 0 1 1 3 2
student= [] 
#print(student)
# insert를 사용
# 처음 받아오는 학생 수는 5명
# 첫 시행은 T번째에 학생을 넣고 첫번째임을 명시
# 두번째 시행은 T-i[1]번째에 2삽입
# 세번째 시행은 T-i[2]번째에 3삽입
# 네번째 시행은 T-i[3]번째에 4삽입
# 마지막 시행은 T-i[4]번째에 5삽입
for num in range(T):
    student.insert(num-i[num],num+1)

for i in student:
    print(i,end=' ')        
