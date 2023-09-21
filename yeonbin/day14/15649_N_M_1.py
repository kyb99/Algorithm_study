# N과 M(1) # 230920

# 길이가 M인 수열 구하기
# nPm을 구하는거임

# 순열 만들기
# 왜 두 개씩 나오지? # 안쓰는 경우에 함수 호출을 한번 더해서 그런거임!
def perm(lev, num):
    if lev == M:
        print(*arr)
        return
    if num == N:
        return
    for i in range(num, N+1):
        if visited[i]:
            continue
        # 사용하는 경우
        arr[lev] = i
        visited[i] = 1
        perm(lev+1, num+1)
        # 원상복구
        visited[i] = 0
        # 아닌경우
        perm(lev, num+1)

N, M = map(int, input().split())
visited = [0] * (N+1)
arr = [0]*M
perm(0, 1)