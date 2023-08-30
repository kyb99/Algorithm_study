from collections import deque
import sys
input = sys.stdin.readline

# 수열의 크기 N
N = int(input())
dq = deque((map(int, input().split())))
# 큰 수들 중에서 가장 왼쪽에 있는 값을 가져와야함
# 수열의 크기가 최대 백만 원소의 크기도 백만까지
# 한 점을 기준으로 오른쪽으로 쭉 순회하기엔 크기가 너무 크다
# 인덱스를 못넣나,..?
contain = []
# 전부 -1로 미리 초기화 있는거만 넣어서 관리하자
res = [-1] * N
idx = 0
while dq:
    # 왼쪽부터 비교
    compare = dq.popleft()
    # 비교할게 있으면 비교 (9 5 4) 
    if contain:
        # 비교할게 있을때 컨테이너의 맨 마지막의 1번인덱스(value)가 새로 들어온거보다 작으면
        if contain[-1][1] < compare:
            # 크기가 안맞을 때까지 해당 항목 반복
            while contain and contain[-1][1] < compare:
                # a는 인덱스 b는 거기있던 값
                a, b = contain.pop()
                # b는 무시하고 들어오는 큰 값을 넣어주면됨
                res[a] = compare
            # 비교 끝났으니까 들어온 친구를 컨테이너로
            contain.append((idx, compare))
        # 왜넣었지...? 일단 혹시 모르니까..?
        else:
            contain.append((idx, compare))
    # 비교할게 없으니까 비교할 애들을 넣어둘 곳에 idx 랑 같이 저장
    else:
        contain.append((idx, compare))
    idx += 1
    
print(*res)
