import sys
input = sys.stdin.readline

# arr의 12345 23456 34567

# bottom - up
def tmp_arr(arr, K, len_arr):
    if len_arr == K:
        return sum(arr)
    # 혹시모를 빈칸 만들기
    con = [0] * 100000
    # 0번째 부터 시작했을때의 값
    con[0] = sum(arr[0:0+K])
    # 1번째 부터 시작했을때 값이 어떻게 바뀌는가
    con[1] = con[0] + (-arr[0] + arr[K])
    # 2번부터 for문 적용
    for i in range(2, len_arr - K + 1):
        con[i] = con[i-1] - arr[i-1] + arr[i+K-1]
    return max(con)

N, K = map(int, input().split())
arr = list(map(int, input().split()))

len_arr = len(arr)
print(tmp_arr(arr, K, len_arr))

