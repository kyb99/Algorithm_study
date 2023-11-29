# try2 # 112329 

# stack으로 풀어야할 것 같은데 어떻게 하는걸까?
# 이것도 시간초과 > .count() 때문이었다!

# Counter 쓰는 것도 알아두자!

import sys
sys.stdin = open('input2.txt')



N = int(input())
arr = list(map(int, input().split()))

num_dict = {}
count_arr = [0] * N
ans = [-1] * N

# for i in range(N):
#     num = arr[i]
#     val = num_dict.get(num)
#     if val == None:
#         num_dict[num] = arr.count(num)
#     count_arr[i] = num_dict[num]

for num in arr:
    num_dict[num] = num_dict.get(num, 0) + 1

print(num_dict)

stack = [-1]*N
top = -1
for i in range(N-1, -1, -1):
    # top이랑 비교해서 top이 크면 그거를 답에 저장하고 push
    # top이 작거나 같으면 pop
    # stack이 비었으면 -1
    if top == -1:
        # push
        top += 1
        stack[top] = arr[i]
    else:
        while top > -1:
            if num_dict[stack[top]] > num_dict[arr[i]]:
                ans[i] = stack[top]
                # push
                top += 1
                stack[top] = arr[i]
                break
            else:
                # pop
                top -= 1
        # push
        top += 1
        stack[top] = arr[i]
    print(stack, top)
print(*ans)