# 알고리즘 스터디 date : 2023-07-31
# 방배정.
# 방의 갯수를 정하는 함수
def get_room(dict,capacity):
    room = 0
    for val in dict.values():
        # val은 인원수
        # 0명이면 방이 필요없음
        if val == 0:
            continue
        #나눠지면 몫만큼 증가
        room += val // capacity
        #만약 남은사람있으면 방하나추가
        #위에서 묶을만큼 묶어서 하나면 될지도?
        if val % capacity != 0:
            room+=1
    return room
        
# 인원수 수용량
number, capacity = list(map(int,input().split()))

# 빈 딕셔너리로 학년과 인원수를 관리
man = {}
girl = {}

for num in range(number):
    gen, grade = list(map(int, input().split()))
    # grade로 학년 구분
    if gen == 0 :
        if grade not in girl:
            girl.setdefault(grade,1)
        else:
            girl[grade] += 1 
    else:
        if grade not in man:
            man.setdefault(grade,1)
        else:
            man[grade] += 1 

# get_room의 리턴을 합해서 출력
result = get_room(man,capacity) + get_room(girl,capacity)
print(result)
