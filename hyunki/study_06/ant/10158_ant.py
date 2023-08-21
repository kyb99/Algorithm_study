import sys
sys.stdin = open('input1.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# t + 1 이면 p,q + 1, 오른쪽 위 45도 방향으로 이동

arr = [[0]* (w+1) for _ in range(h+1)]
print(arr)
'''
+(1,1)
+(1,1)
반사 (-1,1)

반사 (-1,-1)
+(-1,-1)

반사()
'''

