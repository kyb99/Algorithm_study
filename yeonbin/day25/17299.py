# 오등큰수 # 231129
# A에 오른쪽에 있는 수 중 등장한 횟수가 A보다 큰 수 중 가장 왼쪽에 있는 수 
# 없으면 -1

# N의 크기 1~1_000_000 백만

# 시간초과 날것같은데...시간초과난다.
#  .count 바꿔도 이건 시간초과

import sys
sys.stdin = open('input2.txt')

N = int(input())
arr = list(map(int, input().split()))

num_dict = {}
count_arr = [0] * N
ans = [-1] * N

# for num in arr:
#     val = num_dict.get(num)
#     if val == None:
#         num_dict[num] = arr.count(num)
# print(num_dict)

# for i in range(N):
#     num = arr[i]
#     val = num_dict.get(num)
#     if val == None:
#         num_dict[num] = arr.count(num)
#     count_arr[i] = num_dict[num]

for num in arr:
    num_dict[num] = num_dict.get(num, 0) + 1

# print(num_dict, count_arr)

# 맨 마지막은 조사할 필요없음
for i in range(N-1):
    for j in range(i+1, N):
        if count_arr[i] < count_arr[j]:
            ans[i] = arr[j]
            break
# print(count_arr)
print(ans)
