# 넴모넴모(Easy) # 230920

# 1. 격자판의 비어있는 칸을 골라 넴모 올려놓기
# 2. 2*2 사각형 찾아서 없애기
# 3. 없앨 수 있는 넴모가 없으면 게임 그만두기
# 게임을 그만두었을 때 넴모의 배치 가짓수 구하기

# 쓰거나 안쓰거나 그렇게 가보자

di = [[-1, -1, 0], [-1, -1, 0], [0, 1, 1], [0, 1, 1]]
dj = [[-1, 0, -1], [0, 1, 1], [1, 1, 0], [-1, -1, 0]]

# 2*2 사각형이 있는지 확인하기
def check_nemo(i, j):
    for k in range(4):
        cnt = 0
        for dk in range(3):
            ni = i + di[k][dk]
            nj = j + dj[k][dk]
            if 0<=ni<N and 0<=nj<M:
                # 넴모가 없으면
                if arr[ni][nj] == 0:
                    continue
                # 아니면 카운트
                cnt += 1
                if cnt == 3:
                    return True
    return False

def put_nemo(now_i, now_j):
    print(now_i, now_j)
    global ans
    # 이게 마지막 칸이면 카운트 올리고 종료
    if now_i == N:
        ans += 1
        return
    
    is_end = False

    # 이 행에 남은 j 검사
    if now_j != M and now_j != 0:
        for j in range(now_j, M):
            # 이 칸에 넴모를 놓는 경우
            arr[now_i][j] = 1
            is_end = check_nemo(now_i, j)
            # 검사해서 네모다? 그럼 중지
            if is_end:
                return
            # 함수 드가자
            if j == M-1:
                put_nemo(now_i+1, 0)
            else:
                put_nemo(now_i, j+1)

            #  아닌경우
            arr[now_i][j] = 0
            if j == M-1:
                put_nemo(now_i+1, 0)
            else:
                put_nemo(now_i, j+1)
        now_i += 1
    # 다음행 시작부터 검사 / 시작 j==0이면 그행부터임
    for i in range(now_i, N):
        for j in range(M):
            # 이 칸에 넴모를 놓는 경우
            arr[i][j] = 1
            # 첫째 행, 열은 검사할 필요없음
            if i != 0 and j != 0:
                is_end = check_nemo(i, j)
                # 검사해서 네모다? 그럼 중지
                if is_end:
                    return
            # 함수 드가자
            # 끝에 도달했으면
            if j == M-1:
                # 다음행 조사
                put_nemo(i+1, 0)
            else:
                # 아니면 다음칸 조사
                put_nemo(i, j+1)

            #  아닌경우
            arr[i][j] = 0
            if j == M-1:
                put_nemo(i+1, 0)
            else:
                put_nemo(i, j+1)


N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

ans = 0


if N == 1:
    print(2**M)
elif M == 1:
    print(2**N)
else:
    # 판별해서 개수 프린트
    put_nemo(0,0)

    print(ans)