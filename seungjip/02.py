# 일곱 난쟁이 (2309번)
List = []       # 9개의 키가 들어갈 리스트
J = 0           # 나중의 index값 저장을 위해
K = 0           # 동일

for i in range(9):          # 일단 9개의 값을 입력 받아 리스트로 만들기
    N = int(input())
    List.append(N)

Total = -100                # 100은 오바할테니 초과 값만 보기 위해 -100으로 시작
for height in List:         # 리스트를 순회하며 전부 더해가면 초과 값이 Total로 나옴
    Total += height

for j in range(9):                      # 이제 9개 중 합이 Total이 되는 순서쌍을 찾고 싶었음
    for k in range(j+1, 9):             # 그 논리가 악수하는 경우의 수 세는 느낌과 같음
        if List[j] + List[k] == Total:
            J = j                   # 찾은 인덱스 값 저장
            K = k

List.pop(J)         # 그 값 제거
List.pop(K-1)       # 그 세트 제거 J가 더 작기때문에 1을 더 빼야함
List.sort()         # 정렬

for l in List:
    print(l)