# 2477 참외밭 # 230821 다시 도전
# 참외밭 넓이 구하기
# 육각형, ㄱ자로 구성됨
# 반시계 방향으로 밭 둘레 측정했음
# 동1, 서2, 남3, 북4
'''
K
변의 방향 길이
'''
'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''
# 틀림! 다시 풀어야함! 아예 로직을 잘못생각함.

# 긴쪽은 카운트가 1인 곳

# 큰 사각형에서 작은 사각형 빼기
# 긴변 두개가 연속으로 있으면 시작기준 한칸 앞, 두칸앞을 곱하면 됨
# 방향이랑 길이를 묶어서 ㄱ > %6해서 ㄱ
K = int(input())




print((big_area - small_area) * K)

