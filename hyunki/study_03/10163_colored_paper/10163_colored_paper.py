import sys
sys.stdin = open('input1.txt')

N = int(input())

arr = []

for tc in range(N):
    x1, y1, b, h = map(int, input().split())

