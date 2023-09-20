from collections import deque

def bfs():
    global board, answer
    moves = [(1, 0), (0, 1), (-1, 0), (0,- 1)]
    deq = deque([(0, 0, 0)])
    visited = [[[0]*m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = 1
    while deq:
        x, y, z = deq.popleft()
        if x == n-1 and y == m-1:
            return visited[z][x][y]
        for dx, dy in moves:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 방문하지도 않은 경우
                if not board[nx][ny] and not visited[z][nx][ny]:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    deq.append((nx, ny, z))
                # 벽인데 아직 부술 수 있는 기회가 남아있는 경우
                elif board[nx][ny] and z == 0:
                    visited[z + 1][nx][ny] = visited[z][x][y] + 1
                    deq.append((nx, ny, z+1))

    return 1e9


n, m = map(int, input().split())
board = [list(map(int, list(input()))) for i in range(n)]
answer = bfs()
print(-1 if answer == 1e9 else answer)