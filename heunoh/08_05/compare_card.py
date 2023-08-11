# 별4, 동그라미3, 네모2, 세모1

rod = int(input())
# rod는 라운드의 수
for r in range(rod):
    A = list(map(int, input().split())) # A[0] A가 뽑은 카드의 수, 그뒤는 카드
    B = list(map(int, input().split())) # B[0] B가 뽑은 카드의 수
    # 카드는 4종류밖에 없으니까

    A_count = [0] * 4
    B_count = [0] * 4

    # count 리스트에 인덱스는 하나씩 -1해서 저장
    for card in A[1:]:
        A_count[card-1] += 1
    for card in B[1:]:
        B_count[card-1] += 1

    # _count List를 거꾸로 순회하면서 값을 비교
    # 큰값부터 비교해야 함
    # 전부다 같으면 D 출력
    # 카드는 4개밖에 없으니 3210 순으로 인덱스 접근
    for i in range(3, -1, -1):
        if A_count[i] > B_count[i]:
            print("A")
            break
        elif A_count[i] < B_count[i]:
            print("B")
            break
        if i == 0 and A_count[i] == B_count[i]:
            print("D")


