# 용액 # 231108
# 산성 1 ~1_000_000_000
# 염기성 -1 ~ -1_000_000_000
# 합이 특성값
# 같은 양 두 용액 > 합이 0에 가까운 용액 만들기
# 정렬된 순서로 주어짐
# 두 용액 오름차순으로 출력, 여러 경우면 그 중 한 경우 출력
'''
N (2~100_000)
용액들 오름차순 (특성값 모두 다름)
'''
# 시간 초과

N = int(input())
arr = list(map(int, input().split()))

# 전부 산성인 경우
if arr[0] > 0:
    print(arr[0], arr[1])
# 전부 염기성인 경우
elif arr[N-1] < 0:
    print(arr[-2], arr[-1])
else:
    # 맨 끝에서부터 비교, 근데 모든 경우를 다 해봐야하네?
    # 0이 만들어지는 경우 빼고는 뭐가 제일 작은 건지 모르니까
    # 10_000_000_000 : 10억번
    # 두 개의 합이 더 커지는 순간 다음 숫자 조사로 넘어가지
    mini = 9e9
    ans = (0, 0)
    for i in range(N-1):
        late_sum = 0
        # j를 맨 뒤에서부터하나, 아니나 그건 운일듯?
        for j in range(i+1, N):
            tmp = abs(arr[i]+arr[j])
            if tmp == 0:
                ans = (arr[i], arr[j])
                mini = tmp
                break
            if j == (i+1):
                late_sum = tmp
            else:
                # 합이 커진다면
                if tmp >= late_sum:
                    # 다음 i로 ㄱㄱ
                    break # for j
                # 아니라면
                else:
                    late_sum = tmp
                    if late_sum < mini:
                        mini = late_sum
                        ans = (arr[i], arr[j])
        if mini == 0:
            break # for i
    print(*ans)