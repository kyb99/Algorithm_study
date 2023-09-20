# 랜선 자르기 # 230918
# N개의 랜선을 만들어야함
# K개 랜선을 잘라서 N개 같은 길이로
# N보다 많이 만들어도됨
# 최대 랜선 길이

# 이진탐색으로 풀자

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()

if N == 1:
    print(lines[-1])
else:
    pass