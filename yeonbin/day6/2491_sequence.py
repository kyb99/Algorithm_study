# 수열
# 0~9 숫자 N개
# 연속해서 커지거나 연속해서 작아지는 수열(같은거 포함)중 가장 길이가 긴거
# 길이 출력
'''
N
a b *N
'''
# 시간초과 생각안해도됨
# 크거나같다 말고, 크다 / 작다 / 같다 세가지 나눠서 ㄱㄱ

N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(1)

# 증가감소 한번에 할수는 없나?
else:
    s = 0
    e = 1
    # is_des = False # 내림차순인지 확인
    if nums[s] <= nums[e]: #
        is_des = False
    else: # 같은경우 어떻게 관리할지..하..
        is_des = True

    max_len = 2
    cnt = 2
# 답이 없다... 고치려면,,한나절 걸리겠다...
# 4 1 3 3 2 2 9 2 3 의 경우
# 1 3 3 까지 세고, 2 2를 센다
    for i in range(1, N-1):
        print(i, is_des, cnt)
        if is_des == True: # 내림차순
            if nums[i] >= nums[i+1]: # desc
                cnt += 1
                print('a')
                if max_len < cnt:
                    max_len = cnt
            else:
                is_des = False
                if max_len < cnt:
                    max_len = cnt
                cnt = 1
                print('b')
        else:
            if nums[i] <= nums[i+1]: # desc
                cnt += 1
                print('c')
                if max_len < cnt:
                    max_len = cnt
            else:
                if max_len < cnt:
                    max_len = cnt
                is_des = True
                cnt = 1
                print('d')
    # else:
    #     max_len = N
print(max_len)



# two pointer
# print(is_des) # t
# while e < N:
#     print('cmp', s, e, is_des)
#     if is_des == False: # 오름차순
#         if nums[s] <= nums[e]:
#             print('aa') # t
#             e += 1
#             is_des = False
#         else:
#             print('bb')
#             tmp = e-s+1
#             if max_len < tmp:
#                 max_len = tmp
#             s = e
#             e = s + 1
#             is_des = True
#     else: # 내림차순
#         if nums[s] >= nums[e]:
#             print('cc')
#             e += 1
#             is_des = True
#         else:
#             print('dd')
#             tmp = e-s+1
#             if max_len < tmp:
#                 max_len = tmp
#             s = e
#             e = s + 1
#             is_des = False
#     print(s, e)
# tmp = e - s
# if max_len < tmp:
#     max_len = tmp