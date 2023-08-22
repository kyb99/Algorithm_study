import sys
sys.stdin = open('input.txt')

# 두개의 직사강형을 비교
# 겹치면 a, 선이 닿으면 b, 점이 닿으면 c, 안 겹치면 d


for tc in range(4):
    racs = list(map(int, input().split()))

    A = racs[:4]
    B = racs[4:]



