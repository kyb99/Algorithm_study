# 230731
# 일곱 난쟁이
# 일곱 난쟁이의 합이 100

# 난쟁이 찾는 함수
def find_real(dwarfs):
    for i in range(8): # 0 ~ 7
        for j in range(i+1, 9): # i ~ 8
            # print(i,j)
            if all - (dwarfs[i] + dwarfs[j]) == 100:
                dwarfs.pop(i)
                dwarfs.pop(j-1) 
                return dwarfs

dwarfs = []
all = 0 # 난쟁이 키의 합 (9명)
for _ in range(9):
    tmp = int(input())
    dwarfs.append(tmp)
    all += tmp
# print(dwarfs, all) # test
# combination 9C2 = 9*8//2
# 1234567 / 89 ~ 3456789

# # 이중for문이라 break해도 for를 못빠져나옴 > 인덱스 저장해서 나중에 빼기 / 다른 방법은 없나?
# for i in range(8): # 0 ~ 7
#     for j in range(i+1, 9): # i ~ 8
#         print(i,j)
#         if all - (dwarfs[i] + dwarfs[j]) == 100:
#             dwarfs.pop(i)
#             dwarfs.pop(j-1) 
#             break

dwarfs = find_real(dwarfs)
for i in range(6, 0, -1): # bubble sort
    for j in range(0, i):
        if dwarfs[j] > dwarfs[j+1]:
            dwarfs[j], dwarfs[j+1] = dwarfs[j+1], dwarfs[j]

for dwarf in dwarfs:
    print(dwarf)