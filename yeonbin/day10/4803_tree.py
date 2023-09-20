# 트리 # 230904
# 그래프가 주어졌을때, 트리의 개수를 세는 프로그램
# 트리는 사이클이 없는 연결요소
# 정점이 n개, 간선이 n-1개

# 입력으로 주어진 그래프에 트리가 없다면 "No trees."를,
# 한 개라면 "There is one tree."를,
# T개(T > 1)라면 "A forest of T trees."를 테스트 케이스 번호와 함께 출력한다.


# 트리인지 확인 > 사이클이 없는지 확인
# dfs로? bfs로 해서 시작점을 만나는지 보기
# 트리 개수 어떤 기준으로 세는지 잘 모르겠다..!
# 루트를 같이 넘겨준다면..?
# 탐색하다가 루트를 만나면 트리가 아닌걸로?
# .. 모르겟따...
def dfs(now, root):
    global cnt # 트리가 몇개인지..확인하고 싶은데 어떻게 확인하지?
    global is_tree
    if not child[now]: # 자식이 없음
        if is_tree:
            cnt += 1
        return

    # 방문표시하고
    visited[now] = 1
    for i in child[now]:
        if i == root:
            is_tree = False
            return
        if visited[i] == 0: # 안간곳 방문
            dfs(i, root)
    return

tc = 1
N, M = map(int, input().split())
while N!=0:
    # 정점개수, 간선개수
    
    child = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    # print(child)

    for _ in range(M):
        a, b = map(int, input().split())
        child[a].append(b)
        child[b].append(a)
    # print(child)

    cnt = 0
    for i in range(1, N+1):
        is_tree = True
        if child[i] and visited[i]== 0:
            dfs(i, i)

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
    
    tc += 1

    N, M = map(int, input().split())