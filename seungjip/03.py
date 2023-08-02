# 줄 세우기(2605번)
st_num = int(input())

commit = list(map(int, input().split()))
final_list = []

for i in range(st_num):
    final_list.insert(i-commit[i], i+1)

for k in final_list:
    print(k)