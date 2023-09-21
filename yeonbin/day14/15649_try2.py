# pass

def perm(lev, ):
    # arr 마지막까지 채웠으면
    if lev == M:
        print(*arr)
        return
    # 아니라면..arr[lev]를 채워야함
    for i in range(1, N+1):
        if not visited[i]:
            # 쓰는 경우
            visited[i] = 1
            arr[lev] = i
            perm(lev+1)
            # 안쓰는 경우 > 다음 숫자로 넘어감
            visited[i] = 0
    


N, M = map(int, input().split())
visited = [0] * (N+1)
arr = [0]*M
perm(0)