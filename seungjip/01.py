# 방 배정 (13300)
Total, Max_room = map(int, input().split())     # 전체 인원 / 한 방 최대 인원 입력
Male = [0]*6        # 이중 리스트를 만들어 [[남자], [여자]]고 [남자]=[1,2,3,4,5,6학년 인원수들]로 설정
Female = [0]*6 
List = [Male, Female]
Room = 0        # 최종 답이 될 방 개수

for i in range(Total):
    Sex , grade = map(int, input().split())     # 모든 인원 수 만큼 입력 각각 받음( 성별 / 학년 )
    if Sex == 1:                        # 만약 남자라면
        Male[grade - 1] += 1            # 남자의 그 학년에 숫자 1 증가

    else :                              # 여자라면
        Female[grade - 1] += 1          # 여자의 그 학년에 숫자 1 증가

for j in Male:                          # 남자의 1학년부터 순회하며
    if j%Max_room != 0:                 # 만약 나누어 떨어지지 않으면 방을 몫에 다가 +1 추가 해야하고
        Room += j//Max_room + 1
    else :
        Room += j//Max_room             # 나누어 떨어지면 그 몫만큼만 추가

for k in Female:                        # 여자도 마찬가지
    if k%Max_room != 0:
        Room += k//Max_room + 1
    else :
        Room += k//Max_room

print(Room)                         # 결론