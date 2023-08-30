# 탑 # 230830
# N 개의 높이가 다른 탑, 각 탑의 꼭대기에 레이저 송신기
# 수평 왼쪽 방향으로 발사
# 가장 먼저 만나는 탑에만 수신가능
# 각 탑에서 발사한 레이저 신호를 어느탑에서 수신하는지 출력
# 레이저 수신하는 탑 없으면 0출력

# 오큰수랑 방향만 바뀐듯?
# 높이가 같으면 수신할 수 있는건가?

N = int(input()) # 1~500_000
arr = list(map(int, input().split()))

# stack 이용? 레이저..
# 하나씩 넣는데, 크기 비교해서 안에 있는게 작으면 더 큰수 나올때까지 빼고,
#  비었으면 0출력하고 현재거 넣기
# 현재꺼가 작으면 맨 위에꺼 출력하고, 그 위에 내꺼 넣기
# 혹시 몰라서 스택 구현해서 씀
stack = [0] * (N+1)
top = -1
for i in range(N):
    if top == -1: # 스택이 비었으면 0출력하고 push
        print(0, end=' ')
        top += 1
        stack[top] = (arr[i], i+1)
    else:
        if stack[top][0] >= arr[i]: # 안에 있는게 더 클때
            print(stack[top][1], end=' ') 
            # push
            top += 1
            stack[top] = (arr[i], i+1)
        else:
            while True:
                if top == -1:
                    print(0, end=' ')
                    break
                elif stack[top][0] < arr[i]:
                    top -= 1 # pop
                else:
                    break
            if top != -1:
                print(stack[top][1], end= ' ')
            top += 1
            stack[top] = (arr[i], i+1)
    print(stack)
print()







# # 1. bruteforce > 시간초과
# print(0, end=' ')
# for i in range(1, N):
#     if max(arr[:i]) < arr[i]:
#         print(0, end =' ')
#     else:
#         for j in range(i-1, -1, -1):
#             if arr[j] >= arr[i]:
#                 print(j+1, end=' ')
#                 break # for j
# print()

