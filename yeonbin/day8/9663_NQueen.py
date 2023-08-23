# N-Queen
# N*N 판에 퀸 N개를 공격할 수 없게 놓은거
# 놓는 방법의 수 구하기

# 이거..수업시간에 안풀었더니..어케푸는지 모르겟네..
# 완전 탐색?
# 부분집합?
# 처음에 놓고, 가로/세로/대각선을 안되는 표시 해놓기, 퀸 개수 세기
# 다음 열로 넘어가서 되는 칸 찾아서 놓고 반복
# 퀸 개수가 N 개수면 cnt+1
def get_ans(N, queen):
    global cnt
    for i in range(N):
        pass
    # 끝까지 돌았으면 cnt+1
            


    

N = int(input())
board = [0]*N # 인덱스 번호가 열번호, 안의 숫자가 행번호
cnt = 0
get_ans(N, 0, board[:])
print()