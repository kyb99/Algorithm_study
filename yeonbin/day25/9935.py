# 문자열 폭발 # 231129

# 폭발 문자열을 포함하는 경우 폭발문자열 사라짐

# stack을 이용! index 신경쓰자!

import sys
sys.stdin = open('input.txt')

ans = 'FRULA'
string = input()
bomb = input()
N = len(bomb)
stack = []

for cha in string:
    stack.append(cha)
    if cha == bomb[-1] and len(stack)>=N:
        is_same = True
        for i in range(N):
            # 뒤에서 부터 비교하다가 다르면 조사중지
            # print(bomb[N-i-1], stack[-i-1])
            if bomb[N-i-1] != stack[-i-1]:
                is_same = False
                break
        if is_same:
            for i in range(N):
                stack.pop()
if len(stack) > 0:
    ans = ''.join(stack)

print(ans)