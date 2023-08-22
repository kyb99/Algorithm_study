# 2559 수열
# 연속적인 며칠간 최대 온도합
'''
N K 전체 날짜, 연속 날짜
3 -1 .. N
'''

N, K = map(int, input().split())
tempers = list(map(int, input().split()))

# 누적합 구하기
# 바로 앞에꺼 + 지금꺼 = 지금 위치에 저장
for i in range(1, N):
    tempers[i] += tempers[i-1]

# print(tempers) # t
max_v = tempers[K-1] # K번째 날을 처음 최대로 지정 (index: K-1)

for i in range(K, N): # K+1날 부터 조사 (K번째 인덱스부터 조사)
    tmp = tempers[i] - tempers[i-K]
    # print(i, i-K)
    if max_v < tmp:
        max_v = tmp

print(max_v)