# 한 개의 회의실 N개의 회의에 대하여 사용표 작성
# 회의의 수
import sys
input = sys.stdin.readline
N = int(input())
# 시간들을 tuple로 모아둘 리스트
table = []
for _ in range(N):
    start, end = map(int, input().split())
    table.append((start, end))
#table.sort()
#table.sort(key=lambda x:x[0])
table.sort(key=lambda x:x[1])
print(table)
# for i in range(N):
#     tmp = 1
#     if N - i < cnt:
#         break
# 맨 처음 시간의 end를 체커로
checker = table[0][1]
tmp = 1
for i in range(1, N):
    if checker <= table[i][0]:
        checker = table[i][1]
        tmp += 1
print(tmp)
