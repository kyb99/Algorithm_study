import sys
sys.stdin = open('input.txt')

# 회의실은 1개, 사용표 만들기
# 회의 시작시간과 끝시간 주어짐, 회의 시작시간과 끝시간이 같을 수 있음
# 겹치지 않으면서 사용할 수 있는 최대 회의 갯수 찾기기
N = int(input())
meeting = []
max_count = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start,end])

    # 회의 시간 중 i번째를 기준으로
    # 겹치는 부분 remove,
    # 그 다음 올 수 있는 제일 빠르면서 가장 짧은 시간
    # 겹치는 부분 remove,
    # 반복
    # 시간 골라 질때 마다 카운트
    count = 0
    for i in range(N):
        for j in range()


