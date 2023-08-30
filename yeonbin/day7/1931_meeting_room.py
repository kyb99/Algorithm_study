# 회의실 배정
# N개의 회의에 대해 사용표 만들기
# 시작시잔, 종료시간, 겹치지않게 사용하는 회의 최대 개수
# 시작시간, 종료시간 같을수 있음

# 상담하는거...그거랑 똑같은것같은데.. dp..?

# 현오코드 참고 > 난 왜틀렸지?
N = int(input())
meetings = [0] * N
# max_cnt = 0
for i in range(N):
    start, end = map(int, input().split())
    meetings[i] = ((start, end))
    # 회의 시작 시간순서로 정렬하고, 가능한경우, 아닌경우 다 해보기?
meetings.sort(key=lambda x:x[1])
# print(meetings)

check = meetings[0][1]
cnt = 1
for i in range(1, N):
    if check <= meetings[i][0] :
        cnt += 1
        check = meetings[i][1]
        # print(check, cnt)
    
print(cnt)




# 선택하고 / 안하고
# 부분집합 만들어서 가능여부 확인하고 숫자 세기? > 시간초과....
# 2의 10만 제곱...너무 크다..

# def check(meeting):
#     # print(meeting) #t
#     for i in range(len(meeting) - 1):
#         if meeting[i][1] > meeting[i+1][0]: # 회의 끝나는 시간이 다음 회의 시작 시간보다 크다면 불가능
#             return 0
#     return len(meeting)
        

# N = int(input())
# meetings = [0] * N
# max_cnt = 0
# cnt = 0
# for i in range(N):
#     start, end = map(int, input().split())
#     meetings[i] = ((start, end))
#     # 회의 시작 시간순서로 정렬하고, 가능한경우, 아닌경우 다 해보기?
# meetings.sort(key=lambda x:x[0])

# for i in range(1, 1<<N): # 여기서부터 시작
#     tmp = []
#     for j in range(N):
#         if i & (1 << j):
#             tmp.append(meetings[j]) # 회의들 모아놓은 부분집합?
#             if max_cnt < len(tmp):
#                 cnt = check(tmp) # 이 모음이 가능한지 체크
#                 if cnt == 0:
#                     break
#     # print(tmp)
#     # if max_cnt < len(tmp):
#     #     cnt = check(tmp)
    
#     if max_cnt < cnt:
#         max_cnt = cnt
#     # print('cnt, max', cnt, max_cnt)

# print(max_cnt)
