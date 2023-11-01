# n가지 종류의 화학시약
# 용액의 양 m
# ax + b만큼 가스 발생

n = int(input())
candidate = []
for i in range(n):
    a, b = map(int , input().split())
    candidate.append((a,b))
m = int(input())

candidate.sort(reverse=True)

first_a, first_b = candidate[0]; # 4 / 3
# print(first_a, first_b)
# 1씩 증가시키며 확인
result = 0
for i in range(0, m+1):
    # m보다 커지면 종료
    is_valid = True
    compare_gas = first_a * i + first_b
    acc = i
    for j in range(1,n):
        if candidate[j][0] == 0:
            req_solution = compare_gas - candidate[j][1]
        else:
            req_solution = (compare_gas - candidate[j][1]) / candidate[j][0]

        if req_solution % 1 != 0:
            is_valid = False
            break

        if acc + req_solution > m:
            is_valid = False
            break
        else:
            acc += req_solution

    if acc != m:
        is_valid = False

    if is_valid:
        result = compare_gas
        break
print(result)


    






