import sys
sys.stdin = open('input.txt')

# 1개의 회의실, N개의 회의
# 회의의 시작시간과 끝시간 주어짐
# 회의가 끝남과 동시에 다음 회의 시작 가능
# 회의를 최대 사용할 수 있는 최대 개수 출력

N = int(input())
meeting_time = [list(map(int, input().split())) for _ in range(N)]

# 1. 주어진 회의 시간 리스트를 끝나는 시간을 기준으로 오름차순 정렬
meeting_time.sort(key=lambda x: (x[1], x[0]))

# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

# 2. 회의 시간을 N번 순회하면서 시작 값을 기준으로 각각 대입
end_time = 0
meeting_count = 0
for start, end in meeting_time:
    if start >= end_time:
        end_time = end
        meeting_count += 1
print(meeting_count)


