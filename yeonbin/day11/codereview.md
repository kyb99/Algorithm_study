### 승집
- 1인 애들을 하나씩 0으로 만든 다음 bfs를 돌림 > 시간초과
- 경로마다 visited가 똑같으면 안되서 이렇게 한거

### 나
- 처음에 최소라서 bfs로 접근하려고 했는데, 벽부수는것 때문에 dfs로 해봄 (딥카피 이용)
- 근데 시간초과남
- bfs로 하려고 했는데 그냥 틀림

### 흔오
답은 나오지만 틀린코드
- 백트래킹으로 풂, 벽을 부숴보고 유망성조사 > 이후 벽을 못부순다? 그러면 벽 부수기 전으로 돌아가
- 좀 커지면 연산을 못한다.

### 현기
- 이동거리도 카운트, 벽 부수는것도..!
- 한쪽은 이동거리를, 한쪽은 벽 부술수있는지를 카운트 > 그러면 visited가 3차원 배열처럼됨
- bfs로 했음
- 그러네..벽을 부수고 bfs하면 되네..! 벽을 부수고, 안부수고을 그 위치에 같이 저장해주면 되니까..!
- 이해했다..! 아닌듯..ㅎ k번 벽을 부술수있으면 k+1 차원 배열이 된대..
- 이렇게 안하고 큐에 요소 3개 넣어서 하는 방법도 있음
