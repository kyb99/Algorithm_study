# 종이 자르기
# 종이 잘랐을때 가장 큰 종이의 넓이 구하기
'''
입력형식
가로 세로길이(100이하)
N 점선 개수
0/1 점선 *N (가로=0, 세로=1)
'''
# 어떻게 풀어야할까?

width, height = map(int, input().split())
N = int(input())
for i in range(N):
    ch, line = map(int, input().split())
    print(ch, line)
