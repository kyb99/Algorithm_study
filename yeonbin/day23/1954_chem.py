# 화학실험 # 231101
# 96퍼에서 틀림! 뭐가 틀렸을까? 반례를 찾아보자 => N=1인 경우가 문제였음
# 예외 처리 해줘서 pass!
# n가지 종류의 화학시약, M그램 용액
# x그램을 ti에 넣으면 ai*x + bi 만큼 가스 발생
# 각각의 시약에서 같은 양의 가스 발생시키기
# 가능하면 가스양 출력, 불가능하면 0 출력

# a*x +b
# x들을 다 더하면 M이 되어야함

# 어떻게 풀지?
'''
27/3 = 9
3*9 +5 = 32
4*9 +5 = 41
1*9 +5 = 14

a가 작은 순서대로 정렬시켜야하나?

1. 제일 큰거에 1을 넣고, 나머지가 만들어 지는지 확인? 이걸로 ㄱ
2. 자연수의 분할?
3. 조합..?
어렵다...

100*10000 이라서 시간 ㄱㅊ할듯?
'''

arr = []
ans = 0

N = int(input())

for _ in range(N):
    arr.append(tuple(map(int, input().split())))
M = int(input())

# N = 1인 경우 따로 처리
if N == 1:
    ans = arr[0][0]*M + arr[0][1]

if ans == 0:
    # 제일 큰 애부터 숫자 넣을거라서 a 내림차순으로 정렬
    arr.sort(reverse=True)
    # print(arr)

    # 제일 큰애한테 쓸 약품
    for i in range(1, M-N+1):
        # 사용한 약품 양
        acc = i
        # print('i', i)
        maxi = arr[0][0]*i + arr[0][1]
        for j in range(1, N):
            if (maxi-arr[j][1]) % arr[j][0]:
                # 자연수 아니면 다음조사로 넘어가
                # 전부 continue 였다가 아니어서 바꿈!
                break
            tmp = (maxi-arr[j][1]) // arr[j][0]
            # 자연수가 아닌경우 넘어가
            if tmp <= 0:
                break
            # 자연수일 경우, 약물 사용 누적합 구하기
            acc += tmp
            # print('j, x, maxi', j, tmp, maxi)
            # 용량 초과면 돌아가
            if acc > M:
                break
            # 마지막 약품 조사하고, 누적합이 약물양이라면 성공
            if j == N-1 and acc==M:
                ans = maxi
                break
        # 답을 구했다면 조사 더이상 하지마!
        if ans != 0:
            break
print(ans)
