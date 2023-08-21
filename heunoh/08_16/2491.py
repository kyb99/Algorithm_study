T = int(input())
arr = list(map(int, input().split()))


# 예제
# 1 2 2 4 4 5 7 7 2
count = 1
# 길이가 최소 1부터 시작이니까 MAX는 1부터
max_len = 1

for i in range(1, T):
    if arr[i] >= arr[i-1]:
        count += 1
        if count > max_len:
            max_len = count

    elif arr[i] < arr[i-1]:
        if count > max_len:
            max_len = count
        count = 1

count = 1
for i in range(1, T):
    if arr[i] <= arr[i-1]:
        count += 1
        if count > max_len:
            max_len = count

    elif arr[i] > arr[i-1]:
        if count > max_len:
            max_len = count
        count = 1

print(max_len)