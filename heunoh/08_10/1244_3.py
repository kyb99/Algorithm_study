# 구간 정리
# 스위치의 상태를 바꿀 함수
import sys
input = sys.stdin.readline
# 스위치 배열이랑 / 인덱스


def change_switch(position):
    if switch[position] == 0:
        switch[position] = 1
    else:
        switch[position] = 0

T = int(input())
switch = [-1] + list(map(int, input().split()))
N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    arr_len = T
    # 남자일때
    if n == 1:
        for i in range(m, T+1, m):
            change_switch(i)
    # 여자일때
    else:
        change_switch(m)
        for k in range(T//2):
            if m + k > T or m - k < 1:
                break
            if switch[m + k] == switch[m - k]:
                change_switch(m + k)
                change_switch(m - k)
            else:
                break

count = 0
for i in range(1, T+1):
    print(switch[i], end=' ')  # 스위치 상태 출력
    count += 1
    if count % 20 == 0:
        print()
