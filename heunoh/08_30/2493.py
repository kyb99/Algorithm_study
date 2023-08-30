import sys
sys.stdin = open('2493input.txt')

N = int(input())
tower = list(map(int, input().split()))
stack = []
res = [0] * N
# 타워의 마지막 원소를 빼서 새로운 리스트에 넣고
# 새로들어온 거랑 비교, 새로 들어온게 더 크면 출력
# 근데 출력 번호 관리를 어떻게 해야하지?
# 이거도 chekcer 안에 있는 양이 많아지면 오래 걸리지 않나?
# 현기 형님 코드 참고
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])