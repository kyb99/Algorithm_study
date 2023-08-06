# 알고리즘 스터디 date : 2023-07-31
# 백설공주

cm = []
# 입력값을 받아와서 리스트로 관리
for num in range(9):
    tmp = int(input())
    cm.append(tmp)
    
# 합을 받아서 100을 뺀 뒤 난쟁이가 아닌 두친구의 합을 검사하는데 사용 
cm_sum = 0

for num in cm:
    cm_sum += num
    
# cm list에서 합이 cm_sum - 100인 값을 찾기
# 123456이 있다면 12 13 14 15 16검사 후 23 24 25 26을 검사하는식으로
# 반복문 작성
# cm 난쟁이들의 키들의 리스트
# num 각각의 키인데
for num in cm:
    for i in range(9):
        for j in range(i+1,9):
            loop = cm[i] + cm[j]
            # 난쟁이들 키를 합한값에 100을 뺀 값이랑 두수의 합이같으면
            # 임시 변수 생성후 대입
            if loop == cm_sum - 100:
                tmp1 = cm[i]
                tmp2 = cm[j]
                
# for문에서 pop() 으로 삭제하니까 out of range가 나와서
#따로 빼서 삭제
cm.remove(tmp1)
cm.remove(tmp2)

# 정렬된 리스트를 넣어서 출력
result = sorted(cm)
for res in result:
    print(res)    
