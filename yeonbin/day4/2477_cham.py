# 2477 참외밭
# 참외밭 넓이 구하기
# 육각형, ㄱ자로 구성됨
# 밭 둘레 측정했음
# 동1, 서2, 남3, 북4
'''
K
변의 방향 길이
'''
# 틀림! 다시 풀어야함

# 큰 사각형에서 작은 사각형 빼기
K = int(input())
# dir_arr = [[0] for _ in range(5)]
dir_arr = [0] *5
cnt = [0] * 5
sm_h, sm_w, big_w, big_h = 0, 0, 0, 0
for _ in range(6): # 무조건 6번, 6각형
    dir, leng = map(int, input().split())
    if cnt[dir] == 0: # 첫 입력인 경우
        cnt[dir] += 1
        dir_arr[dir] = leng
        # print('dir_a', dir_arr) # test
    elif dir == 1 or dir == 2: # 동 서
        big_w = dir_arr[dir] + leng # 긴변
        sm_w = dir_arr[dir]
        if leng < sm_w:
           sm_w = leng
    else:
        sm_h = dir_arr[dir]
        big_h = dir_arr[dir] + leng
        if leng < sm_h: # 작은 변 구하기
            sm_h = leng
# print(sm_h, sm_w, big_h, big_w)
print(K*(big_h*big_w - sm_h*sm_w)) # 참외 개수 구하기